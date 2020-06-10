from scipy import stats
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import urllib.request
import requests
import MySQLdb
'''
[ANOVA 예제 1]
빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

귀무: 차이없다
대립: 차이있다
'''
list = [[1,64],[2,72],[3,68],[4,77],[2,56],[1,],[3,95],[4,78],[2,55],[1,91],[2,63],[3,49],[4,70],[1,80],[2,90],[1,33],[1,44],[3,55],[4,66],[2,77]]
df = pd.DataFrame(list, columns=['kind','quantity'])
print(df)
df = df.fillna(df.iloc[:,1].mean())
kind1 = df[df.iloc[:,0]==1]
kind2 = df[df.iloc[:,0]==2]
kind3 = df[df.iloc[:,0]==3]
kind4 = df[df.iloc[:,0]==4]
print(kind1,'\n')
# print(kind1.describe(),'\n')
# print(kind2,'\n')
# print(kind2.describe(),'\n')
# print(kind3,'\n')
# print(kind3.describe(),'\n')
# print(kind4,'\n')
# print(kind4.describe(),'\n')


print('1번기름에 대한 shapiro test : ',stats.shapiro(kind1),'\n')
# p-value : 0.01071830466389656 0.05보다 작으므로 정규성 만족x
print('2번기름에 대한 shapiro test : ',stats.shapiro(kind2)[1],'\n')
# p-value : 0.005940891802310944 0.05보다 작으므로정규성 만족x
print('3번기름에 대한 shapiro test : ',stats.shapiro(kind3)[1],'\n')
# p-value : 0.05162493884563446 0.05보다 작으므로 정규성 만족x
print('4번기름에 대한 shapiro test : ',stats.shapiro(kind4)[1],'\n')
# p-value : 0.0037740450352430344 0.05보다 작으므로 정규성 만족x
print('기름들에 대한 등분산성 검정: ',stats.levene(kind1['quantity'],kind2['quantity'],kind3['quantity'],kind4['quantity']).pvalue,'\n')
# p-value 0.3268969935062273 0.05 보다 크므로 등분산성을 만족한다.
# 등분산이 아닌 경우에 사용하는 ANOVA 의 한 방법으로 Welch test 나 Brown-Forsythe test 가 있다.
print('네가지 기름에 대한 f_oneway test',stats.f_oneway(kind1['quantity'],kind2['quantity'],kind3['quantity'],kind4['quantity']),'\n')
# pvalue=0.84824367
print('네가지 기름에 대한 kruskal wallis test',stats.kruskal(kind1['quantity'],kind2['quantity'],kind3['quantity'],kind4['quantity']),'\n')
# KruskalResult(statistic=0.9049322289156589, pvalue=0.8242373884048854)
# p-value가 0.05보다 크므로 귀무가설 채택  기름별로 빵이 흡수하는 기름의 양의 평균의 차이는 통계적으로 유의하지 않다.


'''
[ANOVA 예제 2]
DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
'''
# 귀무가설: 부서별로 직원연봉 평균에 차이가 없다
# 대립가설: 부서별로 직원연봉 평균에 차이가 있다

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

conn = MySQLdb.connect(**config)
sql = 'select buser_name,jikwon_pay from jikwon join buser on buser_no = buser_num'
df = pd.read_sql(sql,conn)

general = df[df.iloc[:,0]=='총무부']
marketing = df[df.iloc[:,0]=='영업부']
system = df[df.iloc[:,0]=='전산부']
managing = df[df.iloc[:,0]=='관리부']

print(general,'\n','\n')
print(general.describe(),'\n','\n')
print(marketing,'\n','\n')
print(marketing.describe(),'\n','\n')
print(system,'\n','\n')
print(system.describe(),'\n','\n')
print(managing,'\n','\n')
print(managing.describe(),'\n','\n')

print('총무부에 대한 shapiro test : ',stats.shapiro(general.iloc[:,1])[1],'\n')
# p-value : 0.02604489028453827 0.05보다 작으므로 정규성 만족x
print('영업부에 대한 shapiro test : ',stats.shapiro(marketing.iloc[:,1])[1],'\n')
# p-value : 0.029116615653038025 0.05보다 작으므로정규성 만족x
print('전산부에 대한 shapiro test : ',stats.shapiro(system.iloc[:,1])[1],'\n')
# p-value : 0.4194071292877197 0.05보다 크므로 정규성 만족O
print('관리부에 대한 shapiro test : ',stats.shapiro(managing.iloc[:,1])[1],'\n')
# p-value : 0.9078023433685303 0.05보다 작으므로 정규성 만족O
print('연봉에 대한 등분산성 검정 : ',stats.levene(general.iloc[:,1],marketing.iloc[:,1],system.iloc[:,1],managing.iloc[:,1]).pvalue,'\n')
# p-value 0.7911993041594357 0.05 보다 크므로 등분산성을 만족한다.
print('부서별 연봉에 대한 일원 ANOVA검정 kruskal: ',stats.kruskal(general.iloc[:,1],marketing.iloc[:,1],system.iloc[:,1],managing.iloc[:,1]).pvalue)
print('부서별 연봉에 대한 일원 ANOVA검정 f_oneway: ',stats.f_oneway(general.iloc[:,1],marketing.iloc[:,1],system.iloc[:,1],managing.iloc[:,1]).pvalue)
#부서별 연봉에 대한 일원 ANOVA검정 kruskal:  0.6433438752252654
#부서별 연봉에 대한 일원 ANOVA검정 f_oneway:  0.7407968978554357
