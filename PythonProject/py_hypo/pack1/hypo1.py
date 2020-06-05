# 분산 / 표준편차의 중요성 - 데이터의 치우침을 표현하는 대표적인 값 중 하나

import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
# 기대값 : 어떤 확률을 가진 사건을 무한 반복할 때 얻을 수 있는 값과 
# 평균으로써 기대할 수 있는 값. 간단하게 평균
print(stats.norm(loc=1, scale=2).rvs(10))

print()
centers = [1, 1.5, 2]
col = ['r','g','b']


print(0.1)




# 표준편차
std = 0.1
data_1   = []
for i in range(3):
    data_1.append(stats.norm(loc=centers[i], scale=std).rvs(100))
    #print(data_1)
    plt.plot(np.arange(len(data_1[i])) + i * len(data_1[0]), data_1[i], '*', color =col[i])
    
plt.show()            
    
std = 2
data_1   = []
for i in range(3):
    data_1.append(stats.norm(loc=centers[i], scale=std).rvs(100))
    plt.plot(np.arange(len(data_1[i])) + i * len(data_1[0]), data_1[i], '*', col)
    
plt.show()