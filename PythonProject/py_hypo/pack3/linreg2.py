import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

score_iq = pd.read_csv('../testdata/score_iq.csv')
print(score_iq.info())
print(score_iq.head())

x = score_iq.iq # 독립변수
y = score_iq.score # 종속변수

# 상관계수
print()
print(np.corrcoef(x, y))
print(score_iq.corr())
plt.scatter(x, y)
plt.show()

# 두 변수 간 인과관계가 있어 보이므로 회귀분석을 수행
# LinearRegressio(), ols()

model =stats.linregress(x, y)
print('model :', model)
# LinregressResult(slope=0.6514309527270075, intercept=-2.8564471221974657, 
# rvalue=0.8822203446134699, pvalue=2.8476895206683644e-50, stderr=0.028577934409305443)


# newx = 140
# yhat = 0.65143 * newx + -2.856447
# print('yhat : ', yhat)

# 기울기
print('slope : ', model.slope)
# 절편
print('intercept :',model.intercept)
# pvalue가 0.5보다 작으면 독립변수로 의미가 있다.
print('pvalue :',model.pvalue) 

