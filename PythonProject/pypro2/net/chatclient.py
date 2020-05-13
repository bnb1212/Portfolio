# 채팅 사용자
import socket
import threading
import sys


def Handle(socket):
    
    #받는 부분
    while True:
        
        data = socket.recv(1024)
        if not data: continue
        print(data.decode('utf-8'))

sys.stdout.flush()

name = input("채팅 아이디 입력: ")
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.193', 7777))
cs.send(name.encode('utf-8')) # 대화명 전송

th = threading.Thread(target=Handle, args=(cs, ))
th.start()


    #주는 부분
while True:
        
    msg = input('>')
    sys.stdout.flush()
        
    if not msg: continue
    cs.send(msg.encode('utf_8')) # 대화내용 전송
        
cs.close()
        
