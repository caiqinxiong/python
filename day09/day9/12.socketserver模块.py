# 并发
import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            conn.send(b'hello')
server = socketserver.ThreadingTCPServer(('127.0.0.1',9001),Myserver)
server.serve_forever()