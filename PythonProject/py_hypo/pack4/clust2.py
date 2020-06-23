'''==============================================
iris로 군집 분석
=============================================='''
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist, squareform

# 데이터 읽기
iris = load_iris()
<<<<<<< HEAD
iris_df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
=======
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
>>>>>>> branch 'master' of https://github.com/bnb1212/Portfolio.git
print(iris_df.head(3))

distmatrix = pdist(iris_df.loc[:, ['sepal length (cm)', 'sepal width (cm)']], 
                   metric='euclidean')
print('distMatrix:',distmatrix)

row_dist = pd.DataFrame(squareform(distmatrix))
print('row_dist: \n', row_dist)

row_clusters = linkage(distmatrix, method='complete')
print('row_clusters :', row_clusters)
df = pd.DataFrame(row_clusters, columns = ['id1', 'id2', '거리', '멤버수'])
print(df)

row_dend = dendrogram(row_clusters)
plt.tight_layout()
plt.ylabel('euclidean dist')
plt.show()
                      