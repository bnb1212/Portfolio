'''===========================================
상관관계 문제)
https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 
그리고 이들의 관계를 heatmap 그래프로 표현하시오
==========================================='''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Advertising.csv"

df = pd.read_csv(url)
print(df)

df = df.loc[:,'tv':'newspaper']
print(df)
print(df.corr())

import seaborn as sns
plt.rc('font', family='malgun gothic')
sns.heatmap(df.corr())
plt.show()