class Memory:

    def process(self,handler,hostname=None):
        ret = handler.cmd('dir', hostname)
        return ret[:10]

