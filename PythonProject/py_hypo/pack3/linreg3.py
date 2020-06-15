'''======================================================
사용빈도가 높은 회귀분석 모델 ols() - 가장 기본적인 결정론적 선형회귀 방법
Ordinary List Square
======================================================'''

import pandas as pd

df = pd.read_csv('../testdata/drinking_water.csv')
print(df.head(3))
print(df.corr())
print()

import statsmodels.formula.api as smf

# 단순 선형 회귀
model = smf.ols(formula = '만족도~ 적절성', data=df).fit() # r style의 모델
# print(model.summary())

print('회귀계수 : ', model.params)
print('결정계수 : ', model.rsquared)
print('p값 : ', model.pvalues)

# 실제값 : 3, 예측값 : 3.735963048858921
print(df.만족도[0], model.predict()[0])

# 시각화
from matplotlib.pylab import plt
import numpy as np

plt.scatter(df.적절성, df.만족도)
# numpy의 polyfit함수
slope, intercept = np.polyfit(df.적절성, df.만족도, 1)
print('slope, intercept :',slope, intercept)
# y = wx + b의 선형회귀선 
plt.plot(df.적절성, slope * df.적절성 + intercept,'lightblue') 
plt.show()

# 다중 선형 회귀
model2 = smf.ols(formula = '만족도 ~ 적절성 + 친밀도', data = df).fit() # R 스타일의 모델
print(model2.summary)

