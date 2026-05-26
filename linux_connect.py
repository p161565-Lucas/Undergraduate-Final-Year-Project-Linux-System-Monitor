import paramiko


class LinuxConnect:
    def __init__(self, hostname, username, password, port=22):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname, username=username, password=password, port=port)

    def exec_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode('utf-8', errors='ignore')

    def exec_script(self, path):
        stdin, stdout, stderr = self.client.exec_command(f'bash {path}')
        return stdout.read().decode('utf-8', errors='ignore')

    def disconnect(self):
        self.client.close()

    def exe_monitor(self,path):
        stdin, stdout, stderr = self.client.exec_command(f'bash{path}')
        return stdout.read().decode('utf-8', errors='ignore')
