# client side
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1' ,8888))
clientsock.sendall('안녕 반가워'.encode(encoding='utf_8')) # 송신

re_msg = clientsock.recv(1024).decode()
print("수신 자료 : " + re_msg)


clientsock.close()


