from conf import settings
from lib.import_class import get_class

def get_server_info(handler,hostname=None):

    info = {}

    for name,string in  settings.PLUGINS_DICT.items():
        cls = get_class(string)
        obj = cls()
        ret = obj.process(handler,hostname)
        info[name] = ret

    return info