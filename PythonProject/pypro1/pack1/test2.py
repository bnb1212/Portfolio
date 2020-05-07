# 집합 자료형 : String, List, Tuple, Set, Dict
# String : 문자열 취급 (순서형), 직접 변경 할 수 없음
s = 'sequence'

print(len(s))  # 문자열 길이 

print(s.count('e'))  # 특정 문자의 갯수

print(s.find('e'), ' ', s.find('e', 3), ' ', s.rfind('e'))  # 문자열 위치 찾기 . rfind는 역순으로 검색

print(s.startswith('s'))  # 문자열 s는 s로 시작하는가 ?

ss = 'mbc'
print('mbc', id(ss))
ss = 'abc'
print('abc', id(ss))  # Garbage Collector가 있음

# ## 문자열 슬라이싱
print(s[0], ' ', s[2:4], ' ', s[:3], ' ', s[3:])
print(s[-1], ' ', s[-4:-1], ' ', s[-4:], ' ', s[::2])

# ## immutable : 수정 불가 
# s[0] = 'k' -> err

# ## 문자열 구분/합치기
ss = 'kbs mbc'
ss2 = ss.split(sep=' ')

print(ss2)
print(','.join(ss2))

# List : 배열과 유사. 순서가 있음. 직접 변경 가능, 여러 종류의 자료를 허용함
print("==========================")
a = [1, 2, 3]
b = [10, a, 12.3, True, 'kbs']
print(a, ' ', id(a))
print(b, ' ', id(b))

# ## 중첩 리스트
print(b[0], ' ', b[1], ' ', b[1][:2])

# ## mutable 변경 가능
b[0] = 'mbc'
print(b[0])

# ## 값에 의한 삭제
b.remove('kbs')
print(b)

# ## 순서에 의한 삭제
del b[3]
print(b)
               
print()
family = ['엄마', '아빠', '나']

# ## 리스트 맨 뒤 삽입
family.append('동생')

# ## 리스트 임의의 지점에 삽입
family.insert(0, '할아버지')
print(family, len(family), family[0])
family.remove('나')

# ## 리스트 여러 요소 더하기
family.extend(['삼촌', '고모', '이모'])
family += ['아주머니', '아조시']

print(family, len(family), family[0])
print()

# ## 기억장소는 값을 갖고 있는 것이 아닌 주소를 기억하고 있는 것 - 참조형 
li = [[0, 1, 2], [3, 4, 5]]
print(li[0])
print(li[0][0])
print()

# ## 얕은 복사 / 깊은 복사 
name = ['tom', 'james', 'oscar']
name2 = name  # 같은 기억장소를 공유
print(name, ' ' , name2)
name[0] = 'sujan'
name2[1] = 'john'
print(name, ' ', name2)

import copy 
name3 = copy.deepcopy(name)  # name3은 name을 복사한 새로운 객체. 주소가 다름. 기억장소 공유 X
print(name, ' ', name3)
name[0] = '길동'
print(name, ' ', name3)
 
# stack 과 queue
sbs = [1, 2, 3]

# ## Last In First Out (LIFO) - stack. 나중에 들어온 놈이 먼저 pop 됨
sbs.append(4)
print(sbs, 'Stack')
sbs.pop()
print(sbs)
sbs.pop()
print(sbs)
print()

# ## First In First Out (FIFO) - Queue. 먼저 들어온 놈이 먼저 pop됨
sbs = [1, 2, 3]

sbs.append(4)
print(sbs, 'Queue')
sbs.pop(0)
print(sbs)
sbs.pop(0)
print(sbs)

 
print("=============================")
