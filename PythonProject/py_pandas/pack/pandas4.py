# 행열 이동, 중복 제거, 구간 단위 설정
import pandas as pd
import numpy as np

df = pd.DataFrame(1000 + np.arange(6).reshape(2, 3), index=['대전', '서울'], columns=['2017', '2018', '2019'])
print(df)

# 행열 이동
print("\n#### 행열 이동 ####")
df_row = df.stack()
print(df_row)

df_col = df_row.unstack
print(df_col)

# 중복 제거
data = {'data1' : ['a'] * 4, 'data2': [1, 1, 2, 2]}
print(data)
df2 = pd.DataFrame(data)
print(df2)

print("\n#### 중복 제거 ####")
result = df2.drop_duplicates()
print(result)

# 연속 데이터 구간 범주화
print("\n#### 연속 데이터 구간 범주화 ####")
price = [10.3, 5.5 , 7.8, 3.6]
cut = [3, 7, 9, 11] # 구간 기준값
result_cut = pd.cut(price, cut)

### (a, b] --> a < x <= b
print(result_cut, type(result_cut))
print(pd.value_counts(result_cut))

print()
datas = pd.Series(np.arange(1, 1001))
print(datas)
# qcut은 데이터를 좀 더 효율적으로 나눌 수 있다.
result_cut2 = pd.qcut(datas, 3)
print(result_cut2)
print(pd.value_counts(result_cut2))

print(" ========================================= ")
# merge
df1 = pd.DataFrame({'data1': range(7), 'key':['b','b','a','c','a','a','b']})
df2 = pd.DataFrame({'key':['b','b','a','c','a','a','b'], 'data2':range(7)})
print(df1)
print(df2)
print()
## 공통 칼럼이 있는경우
### inner join과 비슷하다. 기본값(default)
print(pd.merge(df1, df2, on='key')) # 기본값(default) on='key'))
print(pd.merge(df1, df2, on='key', how='inner'))

print(pd.merge(df1, df2, on='key', how='outer'))
print()
print(pd.merge(df1, df2, on='key', how='left'))
print(pd.merge(df1, df2, on='key', how='right'))


# 공통 칼럼이 없는 경우
df3 =  pd.DataFrame({'key2':['a','b','d'], 'data2':range(3)})
print(pd.merge(df1, df3,  left_on = 'key', right_on='key2'))

print()
# 이어 붙이기
print("\n## 이어 붙이기##")
## 열단위
print(pd.concat([df1, df2], axis=0))
## 행단위
print(pd.concat([df1, df2], axis=1))

## np의 array 자료 이어 붙이기
print('\nnp의 array자료 이어 붙이기')
arr1 = np.arange(6).reshape(2,3)
arr2 = np.arange(4, 10).reshape(2,3)
print(arr1)
print(arr2)
print('\narray 열 이어 붙이기')
arrs1 = np.concatenate([arr1,arr2], axis=0)
print(arrs1)
print('\narray 행 이어 붙이기')
arrs2 = np.concatenate([arr1,arr2], axis=1)
print(arrs2)



