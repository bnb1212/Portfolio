# pandas Module : 고수준의 자료 구조 (Series, Data Frame)을 지원
from pandas import Series
import numpy as np

obj = Series([3, 7, -5, 4])
# 튜플로 만들어도 잘 됨
obj = Series((3, 7, -5, 4))

# Set으로 만들면 에러남
# obj = Series({3, 7, -5, 4})
 
# 자동으로 인덱스가 따라 붙는다.
print(obj, type(obj))

print()
# 인덱스를 직접 지정 가능
obj2 = Series([3, 7, -5, 4], index=['a', 'b', 'c', 'd'])
print(obj2, type(obj2))

# Series의 sum, 파이썬의 sum, numpy의 sum. 
# 파이썬이 제공하는것은 데이터가 많아질 경우 속도가 떨어진다.
print(obj2.sum(), ' ', sum(obj2), ' ', np.sum(obj2))
print(obj2.mean(), obj2.std())
print()
print('배열 값 : ', obj2.values)
print('색인(index) 값 : ', obj2.index)

print('====================== 슬라이싱 =======================================================')
# 색인명, 인덱스번호
print(obj2['a'])
print(obj2[0])
# [] 한번 더 가두어 주면 색인과 값이 같이 나온다.
print(obj2[['a']])
print(obj2[[0]])
print()
print(obj2[['a', 'b']])
# 범위를 줄 수도 있다.
print(obj2['a': 'c'])
print(obj2[2])
print(obj2[2: 4])
print(obj2[[2, 1]])
print(obj2 > 0)
# 값 존재 체크
print("값 존재 체크 a, k")
print('a' in obj2)
print('k' in obj2)

print("============================ dict형 ===================================")
names = {'mouse':5000, 'keyboard' : 350000, 'monitor':550000 }
print(names, type(names))
obj3 = Series(names)
print(obj3)
obj3.index = ['마우스', '키보드', '모니터']
print(obj3)
onames = '상품 가격'

print("============================ DATA FRAME=======================================")
from pandas import DataFrame
df = DataFrame(obj3)
print(df, type(df))

print()
# 각기 다른 세타입을 딕션으로 묶기
data = {
    'irum':['홍길동', '신선해', '공기밥', '한송이', '신기해'],
    'juso':('역상동', '신길동', '역삼동', '역삼동', '서초동'),
    'nai':(23, 30, 35, 40, 42),
    
    }

print(data, type(data))

# 데이터 프레임에 넣어도 알아서 잘 들어간다.
frame = DataFrame(data)
print(frame, type(frame))
# print(frame, ['irum'])
print("=== 이름만 출력 ====")
print(frame.irum)
print(type(frame.irum))
print()
print(DataFrame(data, columns=['juso', 'irum', 'nai']))
frame2 = DataFrame(data, columns=['irum', 'nai', 'juso', 'tel'], \
                    index=['a', 'b', 'c', 'd', 'e'])

print(frame2)

print()
frame2['tel'] ='111-1111'
print(frame2)

val = Series(['222-2222', '333-3333', '444-4444'], index=['b', 'c', 'e'])
frame2['tel'] =val
print(frame2)

print(frame2.T)
print(frame2.values)
print(frame2.values[0, 2])
# 슬라이싱
print(frame2.values[0:2])
print()

# 행삭제
frame3 = frame2.drop('d') 
frame3 = frame2.drop('d', axis = 0)
print(frame3)
frame4 = frame2.drop('tel' ,axis=1) 
print(frame4)

# 정렬
print("================ 정렬 ==================")
print(frame3.sort_index(axis=0, ascending=False))
print(frame3.sort_index(axis=1, ascending=True))
# 사전순으로 순위 매기기
print(frame3.rank(axis=0))

print()
# value_counts 값들의 수
print(frame3['juso'].value_counts())

# 문자열 슬라이싱
print()
data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
    }
frame = DataFrame(data)
print(frame)
result1 = Series([x.split()[0] for x in frame.juso])
result2 = Series([x.split()[1] for x in frame.juso])
print(result1)
print(result2)
print(result2.value_counts())

