'''============================================
과적합(Overfitting) 방지 
============================================'''

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

# print(iris.data)
# print(iris.feature_names)
# print(iris.target)
# print(iris.target_names)

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target
iris_df["target_names"] = iris.target_names[iris.target]

print(iris_df[:5])

# 훈련세트, 테스트세트 나누기
from sklearn.model_selection import train_test_split
# test_size를 30%로, train_size를 70%로 나눈다.
train_set, test_set = train_test_split(iris_df, test_size = 0.3)

print(train_set.shape)
print(test_set.shape)
print('\nLinearRegression)')

# 회귀분석 방법 1 - 선형 회귀(최소제곱)
from sklearn.linear_model import LinearRegression as lm
import matplotlib.pyplot as plt

# train data로 모델 학습
model = lm().fit(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])

# 출력
print(model.score(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])) 
print(model.score(X=test_set.iloc[:, [2]], y=test_set.iloc[:, [3]]))   
print(model.coef_)      #[[ 0.40847816]]
print(model.intercept_) #[-0.33677518]
print('predict \n', model.predict(test_set.iloc[:2, [2]]))

# 시각화
plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='black')
plt.plot(test_set.iloc[:, [2]], model.predict(test_set.iloc[:, [2]]))
plt.show()

print('\nRidge')
# 회귀분석 방법 2 - Ridge: alpha값을 조정하여 과대/과소적합을 피한다.
from sklearn.linear_model import Ridge
model_ridge = Ridge(alpha=10).fit(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])

#점수
print(model_ridge.score(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])) #0.91923658601
print(model_ridge.score(X=test_set.iloc[:, [2]], y=test_set.iloc[:, [3]]))   #0.935219182367
print('ridge predict \n', model_ridge.predict(test_set.iloc[:2, [2]]))

#plot
plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='red')
plt.plot(test_set.iloc[:, [2]], model_ridge.predict(test_set.iloc[:, [2]]))
plt.show()

print('\nLasso')
# 회귀분석 방법 3 - Lasso: alpha값을 조정하여 과대/과소적합을 피한다.
from sklearn.linear_model import Lasso
model_lasso = Lasso(alpha=0.1, max_iter=1000).fit(X=train_set.iloc[:, [0,1,2]], y=train_set.iloc[:, [3]])

#점수
print(model_lasso.score(X=train_set.iloc[:, [0,1,2]], y=train_set.iloc[:, [3]])) #0.921241848687
print(model_lasso.score(X=test_set.iloc[:, [0,1,2]], y=test_set.iloc[:, [3]]))   #0.913186971647
print('사용한 특성수 : ', np.sum(model_lasso.coef_ != 0))   # 사용한 특성수 :  1
print('lasso predict\n', model_ridge.predict(test_set.iloc[:2, [2]]))

plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='blue')
plt.plot(test_set.iloc[:, [2]], model_ridge.predict(test_set.iloc[:, [2]]))
plt.show()

