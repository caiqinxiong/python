from .base import BaseHandler


class AgentHandler(BaseHandler):

    def handler(self):
        # 采集资产信息  cpu disk memory base nic
        # from ..plugins.disk import get_disk
        # ret = get_disk(self)
        from ..plugins import get_server_info
        ret = get_server_info(self)
        print(ret)
        # 向API汇报资产

    def cmd(self, command, hostname=None):
        import subprocess
        ret = subprocess.getoutput(command)
        return ret
