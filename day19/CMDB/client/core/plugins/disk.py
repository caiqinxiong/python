# def get_disk(handler,hostname=None):
#
#     """
#     agent  subprocess
#     ssh  Paramiko
#     salt  salt
#
#     :return:
#     """
#     ret = handler.cmd('dir',hostname)
#     return ret


class Disk:

    def process(self,handler,hostname=None):
        ret = handler.cmd('dir', hostname)
        return ret[:10]

