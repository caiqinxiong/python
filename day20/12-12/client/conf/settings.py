import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENGINE = 'ssh'

ENGINE_DICT = {
    'agent': 'core.engine.agent.AgentHandler',
    'ssh': 'core.engine.ssh.SSHHandler',
    'salt': 'core.engine.salt.SaltHandler',
    'ansible': 'core.engine.ansible.AnsibleHandler',
}

PLUGINS_DICT = {
    'basic': 'core.plugins.basic.Basic',
    'main_board': 'core.plugins.main_board.MainBoard',
    'disk': 'core.plugins.disk.Disk',
    'memory': 'core.plugins.memory.Memory',
    'cpu': 'core.plugins.cpu.CPU',
    'nic': 'core.plugins.nic.NIC',
}

ASSET_URL = 'http://127.0.0.1:8000/api/asset/'

SSH_PORT = 22
SSH_USER = 'root'
SSH_PASSWORD = ''

SSH_KEY = "C:/Users/Administrator/.ssh/id_rsa"

DEBUG = True

FILE_PATH = os.path.join(BASE_DIR, 'files')
