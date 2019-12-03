from .base import BaseHandler


class SaltHandler(BaseHandler):

    def handler(self):
        print('salt')

    def cmd(self, command, hostname):
        import salt.client
        local = salt.client.LocalClient()
        result = local.cmd(hostname, 'cmd.run', [command])
        return result
