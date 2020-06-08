# 집단간 차이 분석 : : 모집단에서 추출한 표본정보를 이용하여 모집단의 다양한 특성을 과학적으로 추론할 수 있다.
# * T-test와 ANOVA의 차이
# - 두 집단 이하의 변수에 대한 평균차이를 검정할 경우 T-test를 사용하여 검정통계량 T값을 구해 가설검정을 한다.
# - 세 집단 이상의 변수에 대한 평균차이를 검정할 경우에는 ANOVA를 이용하여 검정통계량 F값을 구해 가설검정을 한다

# 어느 한 집단의 평균은 0인지 검정하기(난수 사용)
# 귀무 : 자료들의 평균은 0이다.
# 대립 : 자료들의 평균은 0이 아니다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(123)
mu= 0
n = 10
x = stats.norm(mu).rvs(n)
# print(x, np.mean(x))
# sb.distplot(x, kde=False, rug=True, fit=stats.norm) #시각화
# plt.show()

result = stats.ttest_1samp(x, popmean=0)
# print('result:',result)
# result: Ttest_1sampResult(statistic=-0.6540040368674593, pvalue=0.5294637946339893)
# p-value : 0.5294637946339893 > 0.05 이므로 대립가설 기각


result2 = stats.ttest_1samp(x,popmean =0.8)
# print('result:',result2)

# 단일 모집단의 평균에 대한 가설 검정 (one samples t-test)
# 실습 예제 1)
# A 중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리(국어 점수 평균 검정) student.csv

# 데이터 확인
data = pd.read_csv("../testdata/student.csv")
# print(data.head())
print(data.describe())

# 가설
# 귀무 : 국어점수의 평균은 80이다.
# 대립 : 국어점수의 평균은 80이 아니다.

result3 = stats.ttest_1samp(data.국어, popmean=80)
df_mean = data['국어'].mean()
print(df_mean)
print('result2:', result3)
# result2: Ttest_1sampResult(statistic=-1.3321801667713213, pvalue=0.19856051824785262)

# 해석 : p-value 0.19856051824785262 이므로 0.05 보다 크다. 귀무가설 채택. (대립가설 기각)
print('------------------------------------------')
# 실습 예제2)
# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해보자.

# 데이터 확인
data = pd.read_csv('../testdata/babyboom.csv')
# print(data.head())
# print(data.describe())
fdata = data[data.gender == 1]
# print(fdata.head(), len(fdata))
# print(fdata.describe()) -> 여아 몸무게 평균 3132.4g


# 귀무 : 여아 신생아의 몸무게는 평균이 2800(g)이다.
# 대립 : 여아 신생아의 몸무게는 평균이 2800(g)이 아니다.

# 시각화
sns.distplot(fdata.iloc[:, 2], fit=stats.norm)
# plt.show()

stats.probplot(fdata.iloc[:, 2], plot=plt) # Q-Q plot
# plt.show()

print(stats.shapiro(fdata.iloc[:, 2])) # 정규성 확인 p-value : 0.01798 < 0.05이므로 정규성을 따르지 않는다. (0.05보다 크면 따르고, 작으면 따르지 않는다)
# 참고 : 정규성을 띄지 않으나 집단이 하나이므로 wilcox 검정은 할 수 없다.

result4 = stats.ttest_1samp(fdata.weight, popmean=2800)
print('result4 :',result4)
# result4 : Ttest_1sampResult(statistic=2.233187669387536, pvalue=0.03926844173060218)
# 해석 : p-value : 0.039 < 0.05 이므로 귀무 기각.
# 여아 신생아의 몸무게는 평균이 2800(g)보다 크다. 라는 주장을 받아들임 