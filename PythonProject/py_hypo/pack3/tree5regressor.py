'''======================================
DecisionTreeRegressor, RandomForestRegressor ... 등의 모델로 연속형 자료를 예측
========================================'''

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston 
from sklearn.metrics import r2_score

# 보스턴 데이터 불러오기
boston = load_boston()
print(boston.DESCR) # CRIM, ZN, INDUS... : 독립변수
dfx = pd.DataFrame(boston.data, columns=boston.feature_names)
dfy = pd.DataFrame(boston.target, columns=['MEDV'])
df = pd.concat([dfx, dfy], axis=1)
# print(df.head(3))
print(df.corr())

cols = ['MEDV', 'RM', 'PTRATIO', 'LSTAT'] # MEDV와 상관관계가 강한 열 일부 선택
# sns.pairplot(df[cols])
# plt.show()

# 변수 설정
x = df[['LSTAT']].values # 2차원
y = df['MEDV'].values # 1차원
# print(x)
# print(y)

# 실습 1 : DecisionTreeRegressor
model = DecisionTreeRegressor(max_depth=3).fit(x,y)
print('predict : ', model.predict(x)[:3])
print('real : ', y[:3].ravel())

r2 = r2_score(y, model.predict(x))
print('설명력(결정계수) : ', r2) # 0.699, 약 70%의 설명력을 가짐(좋은 편)

# 실습 2 : RandomForestRegressor
model2 = RandomForestRegressor(n_estimators=1000, criterion='mse').fit(x,y) # 예측에서는 mse(평균 제곱 오차)
print('predict : ', model2.predict(x)[:3])
print('real : ', y[:3].ravel())

r2r = r2_score(y, model2.predict(x))
print('설명력(결정계수) : ', r2r) # 0.699, 약 70%의 설명력을 가짐(좋은 편)

# 시각화
plt.scatter(x, y, c='lightblue', label='train data')
plt.scatter(x, model2.predict(x), c='r', label='predict data')
plt.xlabel('LSTAT')
plt.ylabel('MEDV')
plt.legend()
plt.show()

# 새 값으로 예측
import numpy as np

print(x[:3]) # [[4.98][9.14][4.03]]
x_new = np.array([[10],[15],[1]])
print('예상 집 값:', model2.predict())
