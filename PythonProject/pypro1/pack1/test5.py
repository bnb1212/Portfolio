# 제어문
# if
var = 5
if var >= 3:
    print('크구나')
    print('참일때')
    if var >= 5:
        print('5 초과')
else:
    print('거짓')
        
print('계속 1')

jumsu = 80
# jumsu = int(input('점수 : ')) # 입력 받기

if jumsu >= 90:
    print('우수')
elif jumsu >= 70:
    print('보통')
else:
    print('부족')
    
if 90 <= jumsu <= 100:
    res = 'a'
    
elif 70 <= jumsu <= 90:
    res = 'b'
    
else : 
    res = 'c'
    
print(res)

names = ['홍길동' , '신기해', '이기자']
if '홍길동' in names:
    print('친구이름')
else:
    print('누구야')

a = 'kbs'
b = 9 if a == 'kbs' else 11  # a 값이 kbs면 9, 아닐경우 11을 준다
print(b)    

a = 11
b = 'mbc' if a == 9 else 'kbs'
print(b)

print()
a = 6
print(a * 2 if a > 5 else a + 2)

# ## 결과가 참이면 1, 거짓이면 0
a = 7
print((a + 2, a * 2)[a > 5])  # -> 결과가 거짓이므로 0번째 수행 
print()

# while 
a = 1
while a <= 5:
    print(a, end=' ')
    a += 1

print()
colors = ['r', 'g', 'b']
a = 0
while a < len(colors):
    print(colors[a], end=' ')
    a += 1
    
print()
# pop으로 꺼내기
while colors:
    print(colors.pop(), end=' ')

print()

# import time
# sw = input('boom 스위치를 누를까요 ? (y/n)')
# if sw == 'Y' or sw == 'y':
#     count = 5
#     while 1 <= count :
#         print('%d초 남았어요!' % count)
#         time.sleep(1)
#         count -= 1
#     print('폭발~!~! 콰과과과과과쾅콰광콰과광')
# elif sw == 'N' or sw == 'n':
#     print("작업 취소")
# else:
#     print('y 또는 n을 누르시오')
    
a = 0
while a < 10:
    a += 1
    if a == 5: continue
#    if a == 7: break
    print(a)
else:
    print('while 수행')  # while 문이 break가 아닌 조건에 의해 정상적으로 나왔을때 else문 실행
    
import random
num = random.randint(1, 10)
print(num)

# while True: -> 무한 루프
# while 1: -> 무한루프
# while 0: 실행 안함
# while None: 실행 안함

while 1: 
    print('1 ~ 10 사이의 컴퓨터가 가진 숫자를 입력하시오')
    guess = input()
    su = int(guess)
    if su == num:
        print('성공 ! ' * 5)
        break
    elif su < num:
        print('= Up =')
    elif su < num:
        print('= Down =')
    
        
            
