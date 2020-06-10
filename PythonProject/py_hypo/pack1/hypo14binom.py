''' ==============================================================
이항 검정 : 두가지 값을 가지는 확률변수의 분포를 판단하는데 효과적
예 : 10명의 자격증 시험 합격자 중 남자가 6명이었다고 할 때 '남자가 여자보다 합격률이 높다고 할 수 있는가'

binom test
================================================================'''
import pandas as pd
import scipy.stats as stats

data = pd.read_csv("../testdata/one_sample.csv")
# print(data.head(3))
# print(data.survey.unique()) # [1 0]
ctab = pd.crosstab(index=data['survey'], columns='count')
ctab.index = ['불만족', '만족']
print(ctab) # 자바 교육 후 교육 만족 여부 교차표 불만족 14

# 양측 검정 : 방향성이 없다. 기존 80% 만족율 기준 검증 실시
# 형식  stats.binom_test([136. 414] ,p                                                                         
x = stats.binom_test([136, 14], p=0.8, alternative='two-sided') # 양측검정이므로 alternative에 two-sided
print(x) # p-value : 0.0067 < 0.05 귀무기각. 기존(80%) 만족율과 차이가 있다.
# 양측검정에서는 기존 만족율보다 크다, 작다 라는 방향성을 제시하지 않는다.

x = stats.binom_test([14, 136], p=0.2, alternative='two-sided')
print(x)

print("\n")
# 단측 검정 : 방향성이 있다.
# 만족, 불만족 순으로 서술. greater하면 150/136이 기존보다 높은지 알수있다.
x = stats.binom_test([136, 14], p=0.8, alternative='greater')
print(x) # p-value : 0.00031 < 0.05 귀무기각. 기존(80%) 만족율 이상의 효과가 있다.(귀무 : 없다)
# 따라서 기존 20%보다 불만율이 작아졌다라고 할 수 있다.

x = stats.binom_test([14, 136], p=0.8, alternative='less')
print(x)

