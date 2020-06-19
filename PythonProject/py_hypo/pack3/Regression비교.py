'''===================================
연속적 데이터들을 예측할 수 있는 각각의 Regressor들을 비교해보자
==================================='''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

adver = pd.read_csv('../testdata/Advertising.csv')
print(adver.head(3))

feature = np.array(adver.loc[:, 'tv':'newspaper'])
label = np.array(adver.sales)
print(feature[:2])
print(label[:2])

# K-NN 모델 Regressor
print('------------------KNeighbors Regressor---------------------')
kmodel = KNeighborsRegressor(n_neighbors=3).fit(feature, label)
# print(kmodel)
kpred = kmodel.predict(feature)
print('kpred:', kpred[:3])
print('kmodel r2 :', r2_score(label, kpred))


# LinearRegression 모델
print('------------------Linear Regression---------------------')
lmodel = LinearRegression().fit(feature, label)
print(lmodel)
lpred = lmodel.predict(feature)
print('lpred:',lpred[:3])
print('lmodel r2 :', r2_score(label, lpred))

# RandomForest Regressor 모델
print('------------------RandomForest Regressor---------------------')
rmodel = RandomForestRegressor(n_estimators=100, criterion='mse').fit(feature, label)
# print(rmodel)
rpred = rmodel.predict(feature)
print('rpred:',rpred[:3])
print('rmodel r2 :', r2_score(label, rpred))

# XGB Regressor 모델
print('------------------XGBoost Regressor---------------------')
xmodel = XGBRegressor(n_estimators=100).fit(feature, label)
# print(rmodel)
xpred = xmodel.predict(feature)
print('xpred:',xpred[:3])
print('xmodel r2 :', r2_score(label, xpred))
