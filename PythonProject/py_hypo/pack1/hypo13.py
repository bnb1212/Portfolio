'''
========================================================
비율 검정 : 집단의 비율이 어떤 특정한 값과 유의한지 검정
one-sample
A 교육센터에는 100명 중에 45명이 흡연을 한다. 국가 통계를 확인해 보니 국민 흡연율은 35%로 알려져 있다.
이 때 비율이 같은지 검정
========================================================
'''

# 귀무 : 'A 교육센터의 흡연율과 국민 흡연율의 비율은 같다' 
# 대립 : 'A 교육센터의 흡연율과 국민 흡연율의 비율은 같지 않다.'

import numpy as np
from statsmodels.stats.proportion import proportions_ztest

count = np.array([45])
nobs = np.array([100])
val = 0.35

z, p = proportions_ztest(count=count, nobs=nobs, value=val) 
print(z)
print(p)  # pvalue : 0.04444 < 0.05 귀무기각. 비율은 같지 않다.

'''
A 교육센터 300명 중 100명이 햄버거를 먹었고, B 교육센터 400명 중 170명이 햄버거를 먹었다.
두 집단의 햄버거를 먹은 비율의 동일 여부를 검정하시오
''' 

# 귀무 : 비율은 같다
# 대립 : 비율은 같지 않다

count = np.array([100, 170])
nobs = np.array([300, 400])

z, p = proportions_ztest(count=count, nobs=nobs, value=0)  # 비율이 제시되지 않은 경우, value값은 0으로 적는다.
print(z)
print(p) #0.013 < 0.05 # 귀무기각. 비율은 같지 않다.
