# iris dataset으로 시각화

import pandas as pd
import matplotlib.pyplot as plt 

iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/iris.csv")

print(iris_data.info())
print(iris_data.head(3))
print(iris_data.tail(3))

# 1, 3번 칼럼으로 산점도 그리기
# plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
# plt.xlabel('Sepal.Length')
# plt.ylabel('Petal.Length')
# plt.title('iris Data')
# plt.show()

iris_col = iris_data.loc[:, 'Sepal.Length':'Petal.Width']
print(iris_col)

from pandas.plotting import scatter_matrix
# scatter_matrix(iris_col)
# scatter_matrix(iris_col, diagonal='kde')  # hist, bar, kde(커널 밀도 추정 곡선)
# plt.show()

# 꽃 종류별 색 부여 후 산포도(산점도)
print(iris_data['Species'].unique())
print(set(iris_data['Species']))

cols = []
for s in iris_data['Species']:
    choice = 0
    if s == 'setosa':choice = 1
    if s == 'virsicolor':choice = 2
    if s == 'virginica':choice = 3
    cols.append(choice)
print(cols)

# plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'], c=cols)
# plt.xlabel('Sepal.Length')
# plt.ylabel('Petal.Length')
# plt.title('iris Data')
# plt.show()

# seaborn 활용
import seaborn as sns

sns.pairplot(iris_data, hue='Species', height=3)
plt.title('seaborn')
plt.show()

print()
x = iris_data['Sepal.Length'].values
#print(x)

# rugplot
sns.rugplot(x)
plt.show()


# kdeplot
sns.kdeplot(x)
plt.show()


