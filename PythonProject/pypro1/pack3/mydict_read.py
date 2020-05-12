import _ast
from pack2.test19 import bb


print('txt 파일을 읽어 dict로 저장')
with open('mydict.txt', 'r') as ff1:
    aa = eval(ff1.read()) # eval은 보안에 좀 문제가 있음
    print(aa)
    print(type(aa))
    
print()
import ast
with open('mydict.txt', 'r') as ff2:
    aa = ff2.read()
    print(aa)
    print(type(aa))
    bb = ast.literal_eval(aa) # 안전보장
    print(bb)
    print(type(bb))
    

