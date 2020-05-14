# 웹서버 구축
from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 7777
handler = SimpleHTTPRequestHandler

serv = HTTPServer(('192.168.0.87', port), handler)
print("웹서버 시작")
serv.serve_forever()

