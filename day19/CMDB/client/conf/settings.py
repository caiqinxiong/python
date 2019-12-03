ENGINE = 'agent'

ENGINE_DICT = {
    'agent': 'core.engine.agent.AgentHandler',
    'ssh': 'core.engine.ssh.SSHHandler',
    'salt': 'core.engine.salt.SaltHandler',
    'ansible': 'core.engine.ansible.AnsibleHandler',
}


PLUGINS_DICT = {
    'disk': 'core.plugins.disk.Disk',
    'memory': 'core.plugins.memory.Memory',
    'cpu': 'core.plugins.cpu.CPU',
    'nic': 'core.plugins.nic.NIC',
}

SSH_PORT = 22
SSH_USERNAME = 'cmdb'
SSH_PASSWORD = ''
SSH_KEY = ''
