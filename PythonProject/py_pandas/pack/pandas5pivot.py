# 원하는 컬럼을 행이나 열에 위치시키고, 소계 등을 구할때 쓰는것이 피벗(pivot) 테이블

# 그룹화, 피벗(pivot)

import numpy as np
import pandas as pd


data = {'city':['강남','강북','강남','강북'],
        'year':[2010, 2011, 2012, 2012],
        'pop':[3.3, 2.5, 3.0, 2.0]
        }

df = pd.DataFrame(data)
print("==원본 테이블 ==")
print(df)

# 행/열 별 연산
print("\n")
print(df.pivot('city', 'year', 'pop'))

print(df.pivot('year', 'city', 'pop'))
print()
print(df.set_index(['city','year']).unstack())
print(df.set_index(['year','city']).unstack())
print()

# 도시별로 year과 pop 그룹화 
hap = df.groupby(['city'])
print(hap.sum())
# hap = df.groupby(['city'].sum())
print(df.groupby(['city', 'year']).mean())

# 피벗과 그룹테이블의 중간적 느낌. 피벗 테이블
print('======================================')
print(df.pivot_table(index=['city'], aggfunc=np.mean)) # 함수의 이름을 적을 것 ㅇ!!
print(df.pivot_table(index=['city', 'year'], aggfunc=np.mean)) 
print(df.pivot_table(index=['city', 'year'], aggfunc=[len, np.mean])) 
print()
print()
print(df.pivot_table(values=['pop'], index=['city']))
print(df.pivot_table(values=['pop'], index=['city'])) # 기본은 평균(mean)
print(df.pivot_table(values=['pop'], index=['city'], aggfunc=len))
print()
print(df.pivot_table(values=['pop'], index=['year'], columns=['city'], margins=True))
print(df.pivot_table(values=['pop'], index=['year'], columns=['city'], margins=True, fill_value=0))

