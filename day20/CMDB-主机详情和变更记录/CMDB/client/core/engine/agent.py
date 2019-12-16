from .base import BaseHandler
import requests
from conf import settings
import json


class AgentHandler(BaseHandler):

    def handler(self):
        # 采集资产信息  cpu disk memory base nic
        # from ..plugins.disk import get_disk
        # ret = get_disk(self)
        from ..plugins import get_server_info
        info = get_server_info(self)
        print(info)
        # 向API汇报资产
        res = requests.post(
            url=settings.ASSET_URL,
            data=json.dumps(info).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        print(res.json())

    def cmd(self, command, hostname=None):
        import subprocess
        ret = subprocess.getoutput(command)
        return ret
