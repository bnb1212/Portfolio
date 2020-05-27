# pandas 기능
from pandas import Series, DataFrame

# 재색인(re-index) ------------------------
data = Series([1, 3, 2], index=(1, 4, 2))
print(data)

data2 = data.reindex((1, 2, 4))
print(data2)

# 재색인 하면서 값 채우기(보간) -----------
data3 = data2.reindex((1, 2, 3, 4, 5))

# ## NaN 값이 생기게 된다.
print(data3)

print("fill_value")
# fill_value로 채우기
data3 = data2.reindex([1, 2, 3, 4, 5], fill_value=777)
print(data3)

print("ffill")
# method =  'ffill'로 채우기 (이전 값으로 NaN을 채움
data3 = data2.reindex([1, 2, 3, 4, 5], method='ffill')
print(data3)

print("pad")
# method =  'pad'로 채우기 (이전 값으로 NaN을 채움)
data3 = data2.reindex([1, 2, 3, 4, 5], method='pad')
print(data3)

print("bfill")
# method =  'bfill'로 채우기 (다음 값으로 NaN을 채움)
data3 = data2.reindex([1, 2, 3, 4, 5], method='bfill')
print(data3)

print("backfill")
# method =  'backfill'로 채우기 (다음 값으로 NaN을 채움)
data3 = data2.reindex([1, 2, 3, 4, 5], method='backfill')
print(data3)

import numpy as np
print('\n')
# 
df = DataFrame(np.arange(12).reshape(4, 3),
               index=['1월', '2월', '3월', '4월'],
               columns=['강남', '강북', '서초'])
print(df)
print(df['강남'])
print(df['강남'] > 3)
print(df[df['강남'] > 3])

print()
print(df < 3)
df[df<3] = 0
print(df)

print('DataFrame index 슬라이싱 관련 메소드')
# loc : 라벨 지원 , iloc : 숫자지원
print(df.loc['3월'])
print(df.loc['3월', :])

print(df.loc[:'2월'])
print(df.loc[:'2월', ['서초']])
print(df.loc[:'2월', ['서초', '강남']])

print()
print(df.iloc[2])
print(df.iloc[2, :])
print(df.iloc[:3])
# 3행 미만이면서 2열
print(df.iloc[:3, 2])
# 3행 미만이면서 1열부터 3열 미만까지
print(df.iloc[:3, 1:3])

print('\n\n 산술 연산 ================')
s1 = Series([1,2,3], index=['a','b','c'])
s2 = Series([4,5,6,7], index=['a','b','d','c'])
print(s1)
print(s2)
# 인덱스 명끼리 연산. 대응되는 값이 없을경우 NaN이 된다.
print(s1 + s2)
print(s1.add(s2))
print(s1 * s2)

print()

# kbs가 알아서 슬라이싱 되어 컬럼이 된다. 와우~
df1 = DataFrame(np.arange(9.).reshape(3,3), columns=list('kbs'), index=['서울', '인천','수원'])
print(df1)

df2 = DataFrame(np.arange(12.).reshape(4,3), columns=list('kbs'), index=['서울', '인천','일산', '수원',])
print(df2)

print()
print(df1 + df2)
print(df1.add(df2))
print(df1.add(df2, fill_value=0))
print()

print(df1 * df2)
print(df1.mul(df2))
print(df1.mul(df2, fill_value=0))

print()
seri = df1.iloc[0]
print(seri)
print(df1 - seri)