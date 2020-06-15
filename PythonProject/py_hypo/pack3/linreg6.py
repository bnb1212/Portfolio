# mtcars dataset으로 선형 회귀 분석 : LinearRegression

from sklearn.linear_model import LinearRegression
import statsmodels.api 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 폰트
plt.rc('font', family='malgun gothic')

# 데이터 읽어오기
mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data

# matrix로 얻기
x = mtcars[['hp']].values 
y = mtcars[['mpg']].values
print('x \n',x[:3], x.shape)
print('y \n',y[:3], y.shape)

# 시각화
# 산포도
plt.scatter(x, y)
plt.xlabel('마력수')
plt.ylabel('연비')
plt.show()

# LinearRegression()이 기울기(가중치), 절편(bias, 추정된 상수, 편향) 반환
fit_model = LinearRegression().fit(x, y)
print('\n--- fit_model---\n')
print('기울기(가중치) :',fit_model.coef_)
print('절편(편향) :',fit_model.intercept_)

# 참고 : 이번 케이스에서는 나누지 않았지만 기본적으론 dataset을 train / test로 분리 후 모델 학습후 모델 평가. 일반적으로 7:3 으로 분리한다.

# train data로 학습하고, test data로 예측값 보기(모델 평가)
pred = fit_model.predict(x)
print('pred\n',pred[:3])

# 새로운 값으로 연비 추정
new_hp = [[110]]
new_pred = fit_model.predict(new_hp)
print('new_pred :',new_pred[[0][0]])

