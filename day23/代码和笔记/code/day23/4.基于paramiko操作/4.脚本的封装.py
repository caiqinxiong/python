import paramiko

class SSHProxy(object):
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

        self.transport = None

    def open(self):
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, password=self.password)

    def command(self, cmd):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport

        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        return result

    def upload(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, remote_path)
        sftp.close()

    def close(self):
        self.transport.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

if __name__ == '__main__':

    with SSHProxy("123.206.16.61",22,'root','nidaye..!') as ssh:
        ssh.command('df')
        ssh.upload(r'D:\wupeiqi\s27\day01\4.基于paramiko操作\xx', '/data/s27/xx')








