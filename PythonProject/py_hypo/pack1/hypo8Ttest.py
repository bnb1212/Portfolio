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
#-----------------------------------------------------------------------------------------------------------
# 실습 ) 두 가지 교육 방법에 따른 평균 시험 점수에 대한 검정 수행 two_sample.csv
# 귀무 : 두 가지 교육 방법에 따른 평균 시험 점수에 차이가 없다.
# 대립 : 두 가지 교육 방법에 따른 평균 시험 점수에 차이가 있다.
data = pd.read_csv("../testdata/two_sample.csv")
print(data.head(3))
result = data[['method', 'score']]
print(result[:3])

# 데이터 분리
m1 = result[result['method'] == 1]
m2 = result[result['method'] == 2]

score1 = m1['score']
score2 = m2['score']
print(score1)
print(score2)

# NaN은 평균으로 대체
# NaN 확인 : describe(), isnull().sum(), innull(any=')
sco1 = score1.fillna(score1.mean())
sco2 = score2.fillna(score2.mean())

# 분포를 시각화
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(sco1, kde=True, fit=stats.norm) 
sns.distplot(sco2, kde=True, fit=stats.norm)
plt.show() 

# 정규성 확인 함수
print(stats.shapiro(sco1)) # 0.36799 > 0.05이므로 정규성 분포를 이룸
print(stats.shapiro(sco2)) # 0.67141 > 0.05이므로 정규성 분포를 이룸

# 등 분산성
print(stats.levene(sco1, sco2).pvalue)
print(stats.fligner(sco1, sco2).pvalue)
print(stats.bartlett(sco1, sco2).pvalue)

# print(stats.ttest_ind(sco1, scro2))
# 등분산성 : 두 집단의 데이터 분포(분산)가 같은지
print(stats.ttest_ind(sco1, sco2, equal_var = True)) # 등분산성을 만족한 경우
# 해석 : p-value(0.8450) > 0.05 
# Ttest_relResult(statistic=2.0303229870795767, pvalue=0.0450057502344844)

print(stats.ttest_ind(sco1, sco2, equal_var=False)) # 등분산성을 만족하지 않은 경우
#Ttest_relResult(statistic=1.8127433876244892, pvalue=0.10328484007335693)

# 만약 정규성을 만족하지 않은경우
# stats.manwhitneyu()


# stats.wilcoxon()을 사용한다.
# stats.kruskal()