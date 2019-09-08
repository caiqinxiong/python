#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/6'

# 导入模块
import socketserver
from conf.settings import IP_PORT
from core.server import FtpServer
from core.log4 import logging

# 主函数功能 永远启用server服务器
def main():
    logging.info('FtpServer Program Start....')
    server = socketserver.ThreadingTCPServer(IP_PORT, FtpServer)
    server.serve_forever()