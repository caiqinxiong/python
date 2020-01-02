import paramiko

# ############### 用户名和密码
"""
transport = paramiko.Transport(('123.206.16.61', 22))
transport.connect(username='root', password='nidaye..!')

sftp = paramiko.SFTPClient.from_transport(transport)

# 上传文件
# sftp.put(r'D:\wupeiqi\s27\day01\4.基于paramiko操作\xx', '/data/s27/xx')

# 下载文件
sftp.get('/data/s27/xx', 'log.txt')

transport.close()
"""


# ############# 公钥和私钥
import paramiko
private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')
transport.close()


