''' ======================================================
선형회귀(linear regression) 
독립변수(x) : 연속형
종속변수(y) : 연속형

회귀분석은 각 데이터에 대한 잔차제곱합이 최소가 되는 선형회귀식을 도출하는 방법이다.
======================================================='''

# 맛보기, 워밍업
import statsmodels.api as sm
import numpy as np

# scikit learn에서 지원하는 datasets
from sklearn.datasets import make_regression
from astropy.units import yyr

# 난수 만들기
np.random.seed(12)

print('\n방법1------------------------------------')
# 방법 1 : make_regression()을 이용 - 모델이 만들어지지는 않는다.

x, y, coef = make_regression(n_samples=50, n_features=1, bias=100, coef=True)
# coef : 기울기(True일시 기울기도 구해준다)
# bias : 절편

print(x[:3])  # -sample 독립변수
# [[-1.70073563]
#  [-0.67794537]
#  [ 0.31866529]]

print(y[:3])  # -sample 종속변수
# [-52.17214291  39.34130801 128.51235594]

print(coef)  # 기울기 w
# 89.47430739278907

# y = wx + b 89.47430739278907 * x + 100
# 만들어진 예측값
yhat = 89.47430739278907 * -1.70073563 + 100
print('yhat : ', yhat) 

# 결과를 알고싶은 new_x 투입
new_x = 0.5
pred_yhat = 89.47430739278907 * new_x + 100
print('pred_yhat : ', pred_yhat) 

print('\n방법2-----------------------------------------')
xx = x
yy = y

# 방법 2 : Linear Regression()을 이용 - 모델을 만든다.
from sklearn.linear_model import LinearRegression

# 모델생성
model = LinearRegression()
print(model)
# fit()으로 데이터를 학습하여 최적의 모형을 추정함 
fit_model = model.fit(xx, yy)  
print(fit_model.coef_)  # 기울기 89.47430739
print(fit_model.intercept_)  # 절편 100
print()
# 예측값 구하기 1 : 수식을 직접 허용
new_x = 0.5
pred_yhat2 = fit_model.coef_ * new_x + fit_model.intercept_
print('pred_yhat2 : ', pred_yhat2)
print()
# 예측값 구하기 2 : predict()
pred_yhat3 = fit_model.predict([[new_x]])
print('pred_yhat3 : ', pred_yhat3)
print()
# 예측값 구하기 3 : predict()
x_new, _, _ = make_regression(n_samples=5, n_features=1, bias=100, coef=True)
print(x_new)
pred_yhat4 = fit_model.predict(x_new)
print('pred_yhat4 : ', pred_yhat4)

print('\n방법3--------------------------------------')
# 방법3 : ols()을 이용 - 모델을 만든다.
import statsmodels.formula.api as smf
import pandas as pd

# xx는 2차원으로 만들어져있다.
print('xx.shape : ', xx.shape)
 
# 차원축소
x1 = xx.flatten() 
print('x1 : ', x1[:5], x1.shape)
y1 = yy

data = np.array([x1, y1])
df = pd.DataFrame(data.T)
df.columns = ['x1', 'y1']
print(df.head(3))

# ols는 ordinary list square의 약자이다.
# 모델 생성
model2 = smf.ols(formula = 'y1 ~ x1', data=df).fit()

# 요약본 출력(OLS Regression Results)
print()
print(model2.summary())
# Intercept 100, x1 절편 100 기울기(coef) 89.4743

# 기존 독립변수들에 대한 예측값
print()
print(df[:3])
print(model2.predict()[:3])

# 새로운 값에 대한 예측 결과
print()
print('x1 : ', x1[:2])
newx = pd.DataFrame({'x1':[0.5, -0.8]})
predy =model2.predict(newx)
print()
print('예측 결과 : \n', predy)
