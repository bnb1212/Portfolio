# echo server
from socket import *

serversock = socket(AF_INET, SOCK_STREAM) # (종류, 유형)
serversock.bind(('127.0.0.1'), 9999)
serversock.listen(1) # 1~ 5
print('server start')

# cnn =  add  = server
print('from cloent masg0 ,')