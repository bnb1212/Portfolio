'''================================================
iris로 지도/비지도 학습 실습 정리
================================================'''

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
# 지도학습-분류 패키지
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
# 비지도학습-차원학습
from sklearn.decomposition import PCA
# 비지도학습-군집
from sklearn.mixture import GaussianMixture

# 데이터 읽어오기
iris = sns.load_dataset('iris')
# print(iris.head(2))

x_iris = iris.drop('species', axis=1)
y_iris = iris['species']
# print(x_iris[:3])
# print(y_iris[:3])

xtrain, xtest, ytrain, ytest = train_test_split(x_iris, y_iris, random_state=1)

# 지도 학습 중 분류
gmodel = GaussianNB()
gmodel.fit(xtrain, ytrain)  # feature, label
pred = gmodel.predict(xtest)
print('---- GaussianNB ----\n')
print('pred : ', pred[:5])
print('acc : ', accuracy_score(ytest, pred))

# 비지도학습 중 차원 축소(압축, PCA)
pmodel = PCA(n_components=2)
pmodel.fit(x_iris)  # feature
x2d = pmodel.fit_transform(x_iris)
print('\n---- PCA ----\n')
# print(x2d)
iris['pca1'] = x2d[:, 0]
iris['pca2'] = x2d[:, 1]
# - 시각화
sns.lmplot('pca1', 'pca2', hue='species', data=iris, fit_reg=False)
plt.show()

# 비지도학습 중 군집
gmmodel = GaussianMixture(n_components=3, covariance_type='full')
gmmodel.fit(x_iris)  # feature
y_pred_g = gmmodel.predict(x_iris)
print(y_pred_g)
# - 시각화
iris['cluster'] = y_pred_g
sns.lmplot('pca1', 'pca2', hue='species', col='cluster', data=iris, fit_reg=False)
plt.show()
