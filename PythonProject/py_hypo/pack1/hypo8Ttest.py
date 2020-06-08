# 두 집단의 가설 검정 - 실습시 분산을 알지 못하는 것으로 한정
# * 서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
# 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인
# 두 집단에서 얻은 표본을 독립 표본(two samples)이라고 한다.

# 실습 ) 남녀 두 집단 간 파이썬 시험의 평균에 차이가 있는지 검정하시오
# 귀무 : 남녀 두 집단간 파이썬 시험의 평균에 차이가 없다.
# 대립 : 남녀 두 집단간 파이썬 시험의 평균에 차이가 있다.

from scipy import stats
import pandas as pd
from numpy import average

male = [75, 80, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

# two_sample = stats.ttest_ind(male, female)
two_sample = stats.ttest_ind(male, female, equal_var = True) # 등분산성 만족(두 그룹간의 분산이 같다)
print(two_sample)
# Ttest_indResult(statistic=1.1239602672651225, pvalue=0.29362218364475595)
sta, pv = two_sample

print('sta :', sta)
print('pv :', pv)
print(average(male), average(female))
# 해석 : male 평균 83.8 female 평균 72.24
# pvalue : 0.25250 > 0.05이므로 귀무가설 채택 남녀 두 집단 간 파이썬 시험의 평균에 차이가 없다.
# 통계학 적으로는 차이가 없다고 보는것.

# T검정시 정규성, 등분산성 체크해야함

# 실습 )
