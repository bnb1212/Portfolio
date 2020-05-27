import numpy as np
from pandas import DataFrame, Series

# pandas 문제 1)
# 
#   a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오
#   b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No2, No4로 지정하시오
#   c) 각 컬럼의 평균을 구하시오

# 랜덤 생성 / 데이터 프레임 생성
print("#### Quiz 1 ####")
q1_rand = np.random.normal(0, 1, (9, 4))
q1_df = DataFrame(q1_rand, columns=['No1', 'No2', 'No3', 'No4'])
print(q1_df)

# 각 컬럼 평균 구하기
print('\n')
print("== No1_mean ==")
print(q1_df['No1'].mean())

print("== No2_mean ==")
print(q1_df['No2'].mean())

print("== No3_mean ==")
print(q1_df['No3'].mean())

print("== No4_mean ==")
print(q1_df['No4'].mean())

print("\n")
print("#### Quiz 2 ####")
q2_df = DataFrame(np.arange(10, 41, 10), columns=['numbers'], index=['a','b','c','d'])
print(q2_df)
print("\n## 값 뽑아내기 ##")
print("c row : ", q2_df.values[2, 0])
print("a, d row : {0},{1}".format(q2_df.values[0, 0],q2_df.values[3, 0]))

print("\n## 합구하기 ##")
numbers_sum = np.sum(np.array(q2_df.values))
print("numbers의 합 :",numbers_sum)

print("\n## DF에 제곱하기 ##")
# np.square(df)도 있다.
q2_df = q2_df * q2_df
print(q2_df) 

print("\n## 열 추가하기 ##")
q2_df['float'] = [1.5, 2.5, 3.5, 4.5]
q2_df['names'] = ['길동', '오정','팔계', '오공']
print(q2_df)
