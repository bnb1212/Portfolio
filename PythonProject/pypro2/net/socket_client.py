from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect('127.0.0.1' ,9999)
clientsock.sandall('안녕 반가워'.encode(encoding='utf_8', errors='strict'))
clientsock.close()
