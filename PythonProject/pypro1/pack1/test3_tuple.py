# Tuple : 리스트와 유사. 읽기 전용. 리스트보다 속도면에서 강점이 있다.
t = ('a', 'b', 'c', 'a')

print(t, ' ', t.count('a'), ' ', t.index('b'))
print(t[0])
# t[0] = 'm' -> err. 읽기 전용이라 에러가 뜬다.

# ## 튜플을 리스트로 만들어 내용을 변경하고 다시 튜플로 변환
q = list(t)
q[0] = 'm'
t = tuple(q)
print(t)

# ## 튜플 순서 변경
t1 = (1, 2)
print(t1)
a, b = t1
b, a = a, b
t1 = a, b
print(t1)
print()

# ## 요소 값이 하나만 있으면 튜플이 아니다. 콤마(,)를 찍어줘야 비로소 튜플이 됨
kk = (1)
kk2 = (1,)
print(kk, type(kk), kk2, type(kk2))

# Set : 순서 없음. 중복 허용 안됨. 
print("===========================")
a = {1, 2, 3, 1}  # 중복은 알아서 걸러진다.
print(a)
b = {3, 4}
print()
print(a.union(b), "합집합")
print(a.intersection(b), "교집합")
print(a - b, a | b, a & b, "차집합, 합집합, 교집합")
print()
# print(a[0]) -> err. 순서 없음
b.add(5)
print(b)
b.update({6, 7})
b.update((8, 9))
b.update([10, 11])
print(b)

# ## 값에 의한 삭제. discard는 해당 값이 없으면 통과, remove는 해당값이 없다면 err를 뱉어낸다.
b.discard(7)
b.remove(6)
b.discard(7)
# b.remove(6) -> err

print(b)
b.clear()  # 그릇 비우기
print(b)

# ## set에 넣었다 뺴서 중복 자료 제거
li = [1, 2, 1, 2]
s = set(li)
li = list(s)
print(li)

# Dict {key:value} : 인덱스로 검색 x. Key로 검색
mydic = dict(k1=1, k2='mbc', k3=1.2)
print(mydic)

# ## 직접 생성
dic = {'파이썬': '뱀', '자바':'커피', '스프링' :'용수철'}
print(dic, ' ' , len(dic))
# ## key로 value 출력
print(dic['자바'])

# ## dic에 삽입
dic['오라클'] ='예언자'
print(dic)

# ## dic 삭제
del dic['오라클']
print(dic)

# ## dic update
dic['자바'] = 'programming lang'
print(dic)
print(dic['자바'])

# ## key만 출력
print(dic.keys())

# ## value만 출력
print(dic.values())
