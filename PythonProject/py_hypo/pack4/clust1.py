'''============================================================
비지도(Unsupervised) 학습 중 하나인 군집(Cluster) 분석
계층적 군집 분석 : 응집형, 분리형
============================================================'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

np.random.seed(13)

var = ['x', 'y']
labels = ['점0', '점1', '점2', '점3', '점4']
x = np.random.random_sample([5, 2])
df = pd.DataFrame(x, columns=var, index=labels)
print(df)

plt.scatter(x[:, 0], x[:, 1], c='b', marker='o', s=50)
plt.grid(True)
plt.show()

# 거리재기 pdist
from scipy.spatial.distance import pdist, squareform
distmatrix = pdist(df, metric='euclidean')
print('distmatrix :', distmatrix)

row_dist = pd.DataFrame(squareform(distmatrix), columns=labels, index=labels)
print(row_dist)

# 응집형 계층적 클러스터링 수행
from scipy.cluster.hierarchy import linkage 
row_cluster = linkage(distmatrix, method='ward')

df = pd.DataFrame(row_cluster,
                  columns=['클러스터1', '클러스터2', '거리', '클러스터 멤버 수'],
                  index=['클러스터 %d' % (i + 1) for i in range(row_cluster.shape[0])])

print(df)

from scipy.cluster.hierarchy import dendrogram
row_dend = dendrogram(row_cluster, labels=labels)
plt.tight_layout()
plt.ylabel('유클리드 거리')
plt.show()

print()

# 병합 군집 알고리즘
from sklearn.cluster import AgglomerativeClustering
ac = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
labels = ac.fit_predict(x)
print('분류 결과:', labels)

a = labels.reshape(-1, 1)
print(a)
x1 = np.hstack([x, a])
print(x1)

x_0 = x1[x1[:, 2] == 0, :]
x_1 = x1[x1[:, 2] == 1, :]
x_2 = x1[x1[:, 2] == 2, :]

print(x_0)

# 시각화
plt.scatter(x_0[:, 0], x_0[:, 1])
plt.scatter(x_1[:, 0], x_1[:, 1])
plt.scatter(x_2[:, 0], x_2[:, 1])

plt.legend(['cluster0','cluster1','cluster2'])
plt.show()

