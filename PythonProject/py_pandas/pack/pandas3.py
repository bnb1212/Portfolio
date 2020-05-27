# pandas : 기술적 통계와 관련된 함수, NaN

from pandas import Series, DataFrame
import numpy as np

df = DataFrame([[1.4, np.nan], [7, -4.5], [np.NaN, np.NAN], [0.5, -1]], 
                columns = ['one', 'two'])

#원본
print(" #### 원본 ####")     
print(df)

# 1행 drop
print("\n#### 1행 drop ####")
print(df.drop(1))

# NaN이 하나라도 있으면 제거
print("\n#### NaN이 하나라도 있으면 제거 ####")
print(df.dropna())

# how
print("\n#### how를 이용하기 ####")

print("\n## 특정 행(any)이 NaN이기만 하면 제거 ##")
print(df.dropna(how='any'))
print("\n## 모든 행(all)이 NaN일때 제거 ##")
print(df.dropna(how='all'))
# 조건주기
print("\n#### 조건 주기 ####")

print("## 특정 열(one)에 NaN이 있으면 제거 ##")
print(df.dropna(subset=['one']))
# 0으로 채우기. 평균으로 채우고 싶을땐 sklearn모듈의 SimpleInputer
print(print("\n#### 0으로 채우기 ####"))
print(df.fillna(0)) 

# =================================================================
print("===========================================================")
#### 기술적 통계와 관련된 함수
## 열의 합 구하기
print("\n#### 합 구하기 ####")
print("## 열의 합 ##")
print(df.sum())
print(df.sum(axis=0))

## 행의 합 구하기
print("\n## 행의 합 ##")
print(df.sum(axis=1))

# 평균 구하기
print("\n#### 평균 구하기 ####")
print("## 행의 평균 ##")
print(df.mean(axis=1))
print(df.mean(axis=1, skipna = True))
print(df.mean(axis=1, skipna = False))

print("\n## 열의 평균")
print(df.mean(axis=0, skipna = True))
print(df.mean(axis=0, skipna = False))

# 최댓값 / 최솟값 구하기
print("\n#### 최댓값 구하기 ####")
print("## 열의 평균 ##")
print(df.max())
print(df.max(axis=0))

print('\n## 최대값 / 최소값 index를 반환 ##')
print(df.idxmax())
print(df.idxmin())

# 요약 통계량 보여주기
print("\n#### 요약 통계량 ####")
print(df.describe())

print("\n#### 구조 ####")
print(df.info())

# 단어 배열로 시도

print("\n#### 단어배열 ####")
words = Series(['봄', '여름'])
