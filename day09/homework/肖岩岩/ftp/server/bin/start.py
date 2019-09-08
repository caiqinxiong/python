import os
import sys
import socketserver

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)


if __name__ == '__main__':
    from core import server
    from conf.config import Config
    sock = socketserver.ThreadingTCPServer((Config["server_ip"], Config["server_port"]), server.MyServer)
    sock.serve_forever()