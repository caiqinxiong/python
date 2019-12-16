from .base import BaseHandler
from conf import settings
import requests
import json
import paramiko

from concurrent.futures import ThreadPoolExecutor


class SSHProxy(object):

    def __init__(self, hostname, port, username, private_key_path):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.private_key_path = private_key_path
        self.transport = None

    def open(self):
        self.private_key = paramiko.RSAKey.from_private_key_file(self.private_key_path)
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, pkey=self.private_key)

    def close(self):
        self.transport.close()

    def command(self, cmd):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        # ssh.close()
        return result

    def upload(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, remote_path)
        sftp.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class SSHHandler(BaseHandler):

    def __init__(self):
        self.ssh_dict = {}

    def handler(self):
        # 获取今日采集的主机列表
        res = requests.get(
            url=settings.ASSET_URL,
        )
        host_list = res.json()
        print(host_list)

        pool = ThreadPoolExecutor(20)
        # 循环主机列表 连接采集 + 汇报
        for hostname in host_list:
            pool.submit(self.task, hostname['hostname'])

    def cmd(self, command, hostname):
        # private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_KEY)
        #
        # # 创建SSH对象
        # ssh = paramiko.SSHClient()
        # # 允许连接不在know_hosts文件中的主机
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # # 连接服务器
        # ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USERNAME, pkey=private_key,
        #             )
        #
        # # 执行命令
        # stdin, stdout, stderr = ssh.exec_command(command)
        # # 获取命令结果
        # result = stdout.read()
        #
        # # 关闭连接
        # ssh.close()

        ssh = self.ssh_dict.get(hostname)
        if not ssh:
            ssh = SSHProxy(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER,
                           private_key_path=settings.SSH_KEY)
            ssh.open()
            self.ssh_dict[hostname] = ssh

        result = ssh.command(command)

        return result.decode('utf-8')

    def task(self, hostname):
        from ..plugins import get_server_info

        info = get_server_info(self, hostname)  # 采集所有的资产信息

        # 再采集一个主机名
        ssh = self.ssh_dict.get(hostname)
        print(ssh)
        old_hostname = ssh.command('cat ~/cert').decode('utf-8').strip()
        hostname = info['basic']['data']['hostname']

        if old_hostname == hostname:
            # 主机名未变更
            # 只更新硬件信息
            info['action'] = 'update'
        else:
            # 主机名变更
            # 更新硬件信息 + 主机名
            info['action'] = 'host_update'
            info['cert'] = old_hostname
        # 向API汇报资产
        print(info)

        res = requests.post(
            url=settings.ASSET_URL,
            data=json.dumps(info).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        ret = res.json()

        if ret['status'] == '200':
            ssh.command('echo "{}" >  ~/cert'.format(hostname))
        ssh.close()
