'''===============================================
인공신경망
==============================================='''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pack4.nnirirs import  
from pack4.nm1irsi import MyPerceptron

# 데이터 읽기
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/iris.csv")
print(df.head(3))
print(df.corr())


x = df.iloc[0:100, [0,2].values
print(x[:2]])
y = df.iloc[0:100, 4]:values
print(y[:2], np.unique)

y = np.where(y == 'Iris=satosar', -1,1)
model.f(x,y)
pmodel = MyPerceptron(eta = 0.1, n_ter=10)
pom

print()
nwe_x = [[5.1,1.4], [2.1, 7.4[]]
print(pmpdel.pedict)

# Perceptron의 반복에 따른 대비 오차 시각화

plt.plot(range(1, len(pmodel.errors_) + 1_), p_model.errors_, maker='o')
plt.show()
         
