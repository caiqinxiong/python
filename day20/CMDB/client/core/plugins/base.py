from conf import settings

class BasePlugin:

    def __init__(self):
        self.debug = settings.DEBUG
        self.file_path = settings.FILE_PATH

    def get_os(self, handler, hostname=None):
        # ret = handler.cmd('uname')
        # if ret == 'Linux':
        #     return 'linux'
        # else:
        #     return 'win'
        return 'linux'

    def process(self, handler, hostname=None):
        os = self.get_os(handler, hostname)
        func = getattr(self, os)

        return func(handler, hostname)

    def win(self, handler, hostname=None):
        raise NotImplementedError('win must be Implemented')

    def linux(self, handler, hostname=None):
        raise NotImplementedError('linux must be Implemented')
