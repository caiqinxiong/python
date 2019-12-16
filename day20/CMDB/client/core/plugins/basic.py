#!/usr/bin/env python
# -*- coding:utf-8 -*-
import traceback
from .base import BasePlugin
from lib.response import BaseResponse


class Basic(BasePlugin):
    def os_platform(self, handler, hostname):
        """
        获取系统平台
        :return:
        """
        output = handler.cmd('uname', hostname)
        return output.strip()

    def os_version(self, handler, hostname):
        """
        获取系统版本
        :return:
        """
        # output = handler.cmd('cat /etc/issue', hostname)
        # result = output.strip().split('\n')[0]
        # return result

        output = handler.cmd('cat /etc/redhat-release', hostname)

        result = output.strip().split()[3]
        return result

    def os_hostname(self, handler, hostname):
        """
        获取主机名
        :return:
        """
        output = handler.cmd('hostname', hostname)
        return output.strip()

    def win(self, handler, hostname=None):
        raise NotImplementedError('win must be implemented ')

    def linux(self, handler, hostname=None):
        response = BaseResponse()
        try:
            if self.debug:
                ret = {
                    'os_platform': 'linux',
                    'os_version': '6.5',
                    'hostname': 'c2.com'
                }
            else:
                ret = {
                    'os_platform': self.os_platform(handler, hostname),
                    'os_version': self.os_version(handler, hostname),
                    'hostname': self.os_hostname(handler, hostname),
                }
            response.data = ret
        except Exception as e:
            msg = traceback.format_exc()
            response.status = False
            response.error = msg

        return response.dict
