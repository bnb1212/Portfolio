'''======================================
밀도 기반 클러스터링
k-means와 달리 k를 결정하지 않아도 된다.
매개변수 (min_sample, eps)를 잘 조절하면 우수한 클러스터링 수행
======================================'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

# 
x1, y1 = make_moons(n_samples=200, noise=0.05, random_state=0)
# print(x)
print()
# print(y)

plt.scatter(x1[:, 0], x1[:, 1])
plt.show()

# kMeans 클러스터링
km = KMeans(n_clusters=2, random_state=0)
pred1 = km.fit_predict(x1)
print(pred1)


def plotResult(x, y):
    plt.scatter(x[y == 0, 0], x[y == 0, 1], c='blue', marker='o', s=40, label='cluster-1')
    plt.scatter(x[y == 1, 0], x[y == 1, 1], c='red', marker='o', s=40, label='cluster-2')
    plt.legend()
    plt.show()


plotResult(x1, pred1)

# DBSCAN
dm = DBSCAN(eps=0.2, min_samples=5, metric='euclidean')
pred2 = dm.fit_predict(x1)
plotResult(x1, pred2)

    
