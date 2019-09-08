#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/7'

import logging
from conf.settings import log_path

# log格式
fh = logging.FileHandler(filename=log_path, encoding='utf-8')
logging.basicConfig(level=logging.INFO,
                    handlers=[fh],
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s - %(name)s[%(lineno)d] - %(levelname)s -%(module)s:  %(message)s')