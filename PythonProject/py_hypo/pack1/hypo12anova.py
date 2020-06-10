'''
================================
일원분산분석 : 집단 구분 요인 1
================================
'''

import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import urllib.request

#그룹별(3개) 네과목 시험 점수 평균 차이 검정
# 귀무 : 그룹별(3개) 과목 시험점수 차이가 없다.
# 대립 : 그룹별(3개) 과목 시험점수 차이가 있다.

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt"
data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',')
print(data.head(3)) # [[243. 1. ] ... <class 'numpy.ndarray'> 

# data2 = pd.read_csv(urllib.request.urlopen(url))
# print(data2)

# 집단 1의 0열 꺼내기
group1 = data[data[:,1] == 1, 0]
# print(group1)
group2 = data[data[:,1] == 2, 0]
group3 = data[data[:,1] == 3, 0]
print(stats.shapiro(group1))
print(stats.shapiro(group2))
print(stats.shapiro(group3)) # 셋다 0.05 보다 크다 (= 정규성을 만족)

# # 그룹간 데이터들의 분포를 시각화
# plot_data = [group1, group2, group3]
# plt.boxplot(plot_data)
# plt.show()

# 일원 분산 분석 방법1
f_statistic, p_val = stats.f_oneway(group1, group2, group3)
print('일원분산분석 결과 : f_statistic:%f, p_val:%f'%(f_statistic, p_val))
# 일원분산분석 결과 : 그룹별(3걔) 시험점수 차이가 있다는 의견이 통계적으로 유의하다.(p_value < 0.05)


# 일원 분산 분석 방법2 - Linear Model을 속성으로 사용
df = pd.DataFrame(data, columns = ['value', 'group'])
print(df)
lmodel = ols('value  ~ C(group)', df).fit() # C(그룹칼럼...) : 범주형임을 명시적으로 표시
print(anova_lm(lmodel)) # PR(>F) <=p_value 이고 0.043589 < 0.05 이므로 

print('\n---------------------------------------------------\n')
'''
===============================
이원분산분석 : 집단 구분 요인 2
===============================
'''

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt"
data = pd.read_csv(url)
print(data.head(3))
print(data.tail(3))

# 귀무 : 관측자와 태아 수 그룹에 따라 태아의 머리둘레에 차이가 없다
# 대립 : 관측자와 태아 수 그룹에 따라 태아의 머리둘레에 차이가 있다

# 시각화
# plt.rc('font', family='malgun gothic')
# data.boxplot(column='머리둘레', by='태아수', grid=True)
# plt.show() # 태아의 머리둘레는 차이가 있어 보임. 관측자와 상호 작용이 있는 분산분석으로 검정

formula = '머리 둘레 ~ C(관측자수) + C(태아수):C(관측자수)'
lm = ols(formula = formula, data = data).fit()
print(anova_lm(lm))
# 해석 : C(관측자수) PR(>F) 6.497055e-03 < 0.05 이므로 머리둘레에 차이가 있다.
# C(태아수):C(관측자수) 4.611573e-25 < 0.05 이므로 머리둘레에 차이가 있다.
# C(태아수):C(관측자수) PR(>F) 3.295509e-01 > 0.05 이므로 상호작용에 의한 머리둘레에 차이가 없다.
# 관측자수와 태아수는 머리둘레에 영향을 미치나 관측자수와 태아수에 상호작용에 의한 영향은 없다.




print()
# 상호작용 무시
formula2 = ' 머리둘레 ~ C(태아수) + C(관측자수)'
lm2 = ols(formula = formula2, data = data).fit()
print(anova_lm(lm2))

