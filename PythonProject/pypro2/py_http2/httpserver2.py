# simpleHTTPRequest를 확장한 CGIHTTPRequestHandler 사용 
# py 문서내에서 html tag를 사용

from http.server import CGIHTTPRequestHandler, HTTPServer

port = 8888


class Handler(CGIHTTPRequestHandler):
    cgi_directories = ['/cgi-bin']


serv = HTTPServer(('192.168.0.87', port), Handler)
print("웹서버 시작")
serv.serve_forever()
