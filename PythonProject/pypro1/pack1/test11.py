# 사용자 정의 모듈 연습
print('이런 저런 작업을 하다가')

import pack1.mymod1  # 같은 패키지 안에 있어도 패키지 명을 적어야한다.
print(dir(pack1.mymod1))

list1 = [1, 2]
list2 = [3, 4, 5]

pack1.mymod1.ListHap(list1, list2)

# 여러 모듈 중 응용프로그램 시작 모듈을 명시적으로 표시하기
if __name__ == '__main__':
    print("나는 최상위 메인 모듈")
    
# 1)
pack1.mymod1.kbs()

# 2)
from pack1 import mymod1
mymod1.kbs()

# 3)
from pack1.mymod1 import kbs, Mbc, gvar
kbs()
Mbc()
print(gvar)

print('=====' * 10)
from etc.mymod2 import *
print(Hap(5, 3))
print(Cha(5 , 3))

# 패스에 추가한 모듈
print('=====' * 10)
import mymod3
print(mymod3.Gob(4, 3))
from mymod3 import Nanugi
print(Nanugi(4, 3))

print(dir(str))