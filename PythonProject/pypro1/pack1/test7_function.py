# 함수 : 실행 단위
# 내장 함수

# ## 리스트 합
print(sum([3, 5, 7]))

# ## 자료형 변환
print(int(1.7), float(4), str(5) + '오')

# ## 반올림
print(round(1.2), round(1.6))

import math
# ## 정수 근사치 중 큰 수 ( 올림 )
print(math.ceil(1.2), math.ceil(1.6)) 
# ## 정수 근사치 중 작은 수 ( 버림 )
print(math.floor(1.2), math.floor(1.6))

x = [10, 20, 30]
y = ['a', 'b']
# ## 쌍을 만들어 주는 zip
for i in zip(x, y):
    print(i)
    
# ## ... 이외에도 많은 내장 함수가 있다.

# 사용자 정의 함수
print("=====" * 10)


def DoFunc1():
    print('DoFunc1')

    
print(DoFunc1)  # 함수 주소 출력
DoFunc1()
kbs = DoFunc1
kbs()


def DoFunc2(a, b):
    print('DoFunc21')
    result = DoFunc3(a, b)
    return result


def DoFunc3(m, n):
    imsi = m + n
    return imsi


mbc = DoFunc2
print(mbc(5, 6))
print(mbc('대한', '민국'))

print('현재 사용중인 객체 목록: ', globals())

print()


def isOdd(arg):
    return arg % 2 == 1


myDict = {x:x * x for x in range(11) if isOdd(x)}
print(myDict)

# 전역변수, 지역변수
print("=====" * 10)
player = '전국 대표'  # 모듈의 멤버. global variable. 전역 


def FuncSoccer():
    name = '무투가켄'  # local variable. 지역
    print(name, player)


FuncSoccer()
print(player)
# print(name)

print()
a = 10; b = 20; c = 30
print('1) a: ', a, 'b: ' , b, ', c:', c)


def Good():
    a = 40
    b = 50
    print('2) a: ', a, 'b: ' , b, ', c:', c) 
    

    def Nice():
        #c = 60
        global c # 모듈의 멤버(최상위)를 찾아감
        nonlocal b # 자신 상위 함수의 멤버를 찾아감 - 잘 안씀
        
        print('3) a: ', a, 'b: ' , b, ', c:', c)
        c = 60 # err : local variable 'c' referenced before assignment (위의 global c 서술 안했을경우 )
        b = 70 
    Nice()
    print('4) a: ', a,'b: ' ,b, ', c:',c)
    
Good()
print('5) a: ', a, 'b: ' ,b, ', c:',c)