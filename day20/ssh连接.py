import paramiko

# hostname = '192.168.36.189'
hostname = 'c1.com'
SSH_PORT = 22
SSH_USER = 'root'
SSH_PASSWORD = '123456'
SSH_PRIVATE_KEY = "C:/Users/Administrator/.ssh/id_rsa"

command = 'uname'  # 操作系统
command = 'cat /etc/issue'  # 系统版本
command = 'hostname'  # 主机名
command = 'cat /proc/cpuinfo'  # cpu
command = 'sudo MegaCli  -PDList -aALL'  # 硬盘
command = 'sudo dmidecode -t1'  # 主板
command = 'sudo dmidecode  -q -t 17 2>/dev/null'  # 内存
command = 'cat ~/cert'
# command = 'echo "c1.com" > ~/cert'

private_key = paramiko.RSAKey.from_private_key_file(SSH_PRIVATE_KEY)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, port=SSH_PORT, username=SSH_USER, pkey=private_key, )
stdin, stdout, stderr = ssh.exec_command(command)

result = stdout.read()

ssh.close()
print(result.decode('utf-8').strip())
