import paramiko

ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='123.206.16.61', port=22, username='root', password='nidaye..!')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()
print(result.decode('utf-8'))
# 关闭连接
ssh.close()

transport = paramiko.Transport(('123.206.16.61', 22))
transport.connect(username='root', password='nidaye..!')

sftp = paramiko.SFTPClient.from_transport(transport)

# 上传文件
# sftp.put(r'D:\wupeiqi\s27\day23\4.基于paramiko操作\xx', '/data/s27/xx')

# 下载文件
sftp.get('/data/s27/xx', 'log.txt')

transport.close()