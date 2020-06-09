# 세 개 이상의 모집단에 대한 가설 검정
# 분산 분석 '분산분석' 이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고
# 요인에 의한 분산이 의미 있는 크기를 가지는지를 검정하는 것을 의미한다.
# 세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제 1종 오류가 증가하게 되어 문제가 발생한다.
# 이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.
# 종속변수의 변화 폭(분산)이 독립 변수에 의해 주로 기인하는 지를 파악할 때 사용

# * 서로 독립인 세 집단의 평균 차이 검정 : 독립변수-범주형, 종속변수: 수치형

# 실습 ) 세 가지 교육방법을 적용하여 1개월동안 교육받은 교육생 80명을 대상으로 실기시험을 실시.
# 일원 분산 분석(one-way anova)
# 귀무 : 세가지 교육방법(3집단)에 교육방법에 따른 실기시험에 평균에 차이가 있다.
# 대립 : 세가지 교육방법(3집단)에 교육방법에 따른 실기시험에 평균에 차이가 있다.

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols

data = pd.read_csv('../testdata/three_sample.csv')
# print(data.head(3), ' ',len(data))
# print(data.describe())

# import matplotlib.pyplot as plt
# # plt.hist(data.score)
# plt.boxplot(data.score)
# plt.show()

# 이상치 제거
data = data.query('score <= 100')
print(data.describe())

# 정규성 확인
print('정규성 만족 여부:', stats.shapiro(data.score)[1]) # 0.2986 > 0.05 ok

# 등분산성 확인
result = data[['method', 'score']]
print(result)
m1 = result[result['method'] ==1]
m2 = result[result['method'] ==2]
m3 = result[result['method'] ==3]
print(m1)
score1 = m1['score']
score2 = m2['score']
score3 = m3['score']
print(score1[:3])

# 모수 검정
print("등분산성 확인 :", stats.levene(score1, score2,score3).pvalue) 
print("등분산성 확인 :", stats.fligner(score1, score2,score3).pvalue)
# 비모수 검정
print("등분산성 확인 :", stats.bartlett(score1, score2,score3).pvalue) 

# 등분산성 확인 : 0.11322850654055751 > 0.05 등분산성 만족이므로 anova 사용. 아니라면 welchi's anova
# 등분산성 확인 : 0.10847180733221087
# 등분산성 확인 : 0.15251432724222921


print('\n가공된 자료로 분산분석')
# 교차표 : 교육방법별 건수
data2 = pd.crosstab(index=data['method'], columns=['count'])
data2.index = ['방법1','방법2','방법3']
print(data2)

# 교차표 : 교육방법별 만족 여부
data3 = pd.crosstab(data['method'], data['survey'])
data3.index = ['방법1','방법2','방법3']
data3.columns = ['만족', '불만']
print(data3)

# f 통계량 얻기 위해 단순 회귀분석 결과를 이용 (독립 변수 1개)
# 단순 선형 회귀 모델 작성
reg = ols('data["score"] ~ data["method"]', data=data).fit()
print(reg)

import statsmodels.api as sm
table =sm.stats.anova_lm(reg, typ=1)
print(table) # PR(>F) <- 이걸 p-value라고 생각하자. 0.72759 > 0.05 이므로 귀무가설 채택.
# 세 가지 교육방법에 따른 실기시험의 평균에 차이가 없다.

# F 통계량을 얻기위해 다중 회귀 분석 결과를 이용 (독립변수 복수개)
'''
reg2 = ols('data["score"] ~ data["method"] + data["survey"]'  , data=data).fit()
print(reg2)
table2 = sm.stats.anova_lm(reg2, typ=1)
print(table2)
'''
# sum_sq -> 제곱합(ssr)
# mean_sq -> 평균 제곱합(msr)

# 분산분석은 전체 그룹 간의 평균값 차이가 유의미한지 검정
# 하지만 어느 그룹의 평균값이 의미가 있는지는 알려주지 않는다.
# 그래서 사후 검정(Post Hoc Test)을 한다.
# 여기서 등분산이 가정되었을때 Scheffe, Tukey 또는 Duncan을 많이 사용합니다.
# 등분산이 가정되지 않았을 때 Dunnett T3 또는 Games-Howell을 사용합니다.

# Tukey 사용(비교대상 표본수가 동일한 경우 사용 : 가장 일반적인 방법)
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey_result = pairwise_tukeyhsd(data.score, data.method) # data['method']
print(tukey_result) # reject = True(유의미한 차이), reject = False (유의미한 차이가 없다)  

import matplotlib.pyplot as plt

# 시각화
tukey_result.plot_simultaneous()
plt.show()
