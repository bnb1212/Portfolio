# 모듈 ( module ) : 코드의 재 사용을 가능하게 하며, 하나의 이름 공간으로 별도 관리가 가능하다.
# module은 package 내에서 작성해야 한다.

print('뭔가를 하다가 ... ')
a = 10
print(a)


def aa():
    pass


# 표준 모듈 sys
import sys 
print(sys.path)
# sys.exit()
# print('종료')
print("=====" * 10)

# 표준 모듈 math
import math
print(math.pi)
print(math.sin(math.radians(30)))
print("=====" * 10)

# 표준 모듈 calendar
import calendar
calendar.setfirstweekday(6)
calendar.prmonth(2020, 5)
print("=====" * 10)

# 표준 모듈  random
import random
print(random.random())
print(random.randrange(1, 10))

from random import random, randrange # from 모듈명 import 멤버명; 앞에 모듈명 쓰지 않고 멤버들을 쓰고 싶을때
print(random())
print(randrange(1, 10))

from random import * # 랜덤 모듈의 모든 멤버 가져다 쓰기. 하지만 좋은 방법은 아니다. 

from turtle import *
p = Pen()
p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()
done()




