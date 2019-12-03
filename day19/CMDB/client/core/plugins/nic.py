class NIC:

    def process(self,handler,hostname=None):
        ret = handler.cmd('ipconfig', hostname)
        return ret[:10]

