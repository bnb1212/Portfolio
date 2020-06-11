
'''====================================
db자료를 읽어 이를 근거로 가설검정 정리
===================================='''

import MySQLdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
import scipy.stats as stats
from distributed.profile import plot_data

with open('mariadb.txt', 'r') as f:
    config = f.read()
    
# db정보를 가진 config(dict type)
config = ast.literal_eval(config)
print(config)

conn = MySQLdb.connect(**config)

cursor = conn.cursor()

sql = """
select jikwon_no, jikwon_name, jikwon_jik, jikwon_pay 
from jikwon 
where jikwon_jik = '과장' and jikwon_pay >= 7500
"""

cursor.execute(sql)

for data in cursor.fetchall():
    print('%s %s %s %s' % data)
    
print('\n -------------------------------------------\n') 
'''====================================================
교차분석(이원 카이제곱 검정) 
변수 두가지
===================================================='''

df = pd.read_sql("select * from jikwon", conn)
# print(df.head(), df.shape) # 30행 8열

print("각 부서(범주형)와 직원평가점수(범주형) 간의 관련성 분석")
# 요인이 모두 범주형이니 카이제곱 사용

buser = df['buser_num']
rating = df['jikwon_rating']

ctab = pd.crosstab(buser, rating)  # 교차표 작성
print(ctab)
chi, p, df, exp = stats.chi2_contingency(ctab)
print('chi:{:.3f}, p:{:.3f}, df:{}'.format(chi, p, df))
# chi:7.339, p:0.291, df:6
# 해석1 : 카이제곱표에서 임계치 12.59 > 7.339이므로 귀무 채택
# 해석2 : p-value > 0.05 이므로  귀무채택

print('\n--------------------------------------------\n')
'''=====================================================
두 집단 이하의 평균차이 분석( t 검정)
독립변수 : 범주형
종속변수 : 연속형
====================================================='''

print("10번, 20번 부서 간 평균 연봉 차이 여부를 검정")
# 귀무 : 두 부서 간 연봉 평균에 차이가 없다.
df_10 = pd.read_sql('select buser_num, jikwon_pay from jikwon where buser_num=10', conn)
df_20 = pd.read_sql('select buser_num, jikwon_pay from jikwon where buser_num=20', conn)
print(df_10.head(2))
print(df_20.head(2))

buser10 = df_10['jikwon_pay']
buser20 = df_20['jikwon_pay']

# 정규성 체크 
print(stats.shapiro(df_10['jikwon_pay'])) 
print(stats.shapiro(df_20['jikwon_pay']))  # 둘다 정규성을 만족하지 않음

# 등분산성 체크
# print(stats.levene(df_10, df_20))

# 정규성을 만족하지 않으므로 다른 검정을 사용해야하지만, 일단 pass
t_result = stats.ttest_ind(buser10, buser20)
print(t_result)
# Ttest_indResult(statistic=0.4585177708256519, pvalue=0.6523879191675446)

print(np.mean(buser10), ' ', np.mean(buser20))  # 5414.28   4908.33
# 해석 : p-value=0.6455 > 0.05 이므로 귀무 채택
# 두 부서의 평균은 통계적으로는 차이가 없다라고 볼수 있다

print('\n-----------------------------------------------\n')
'''=======================================================
세 집단 이상의 평균에 대한 분산분석(ANOVA, f 검정) 
독립변수 : 범주형
종속변수 : 연속형 
======================================================='''
print('각 부서간(4개) 평균 연봉 차이 여부를 검정')
df3 = pd.read_sql('select * from jikwon', conn)
print(df3.head(2))
group1 = df3[df3['buser_num'] == 10]['jikwon_pay']
print(group1[:2])
group2 = df3[df3['buser_num'] == 20]['jikwon_pay']
group3 = df3[df3['buser_num'] == 30]['jikwon_pay']
group4 = df3[df3['buser_num'] == 40]['jikwon_pay']

# 데이터 분포 시각화
from statsmodels.formula.api import ols
import statsmodels.api as sm
import matplotlib.pyplot as plt

plot_data = [group1, group2, group3, group4]
# plt.boxplot(plot_data)
# plt.show()

# 일원 분산 분석 1 (one-way)
f_sta, p_val = stats.f_oneway(group1, group2, group3, group4)
print('---- 결과 ---- \nf_sta : {0:.3f}\np_val :{1:.3f}'.format(f_sta, p_val))
# f_sta : 0.412 p_val :0.745
# 해석 : p_val : 0.745 > 0.05 이므로 귀무 채택

# 일원분산분석
lmodel = ols('jikwon_pay ~ C(buser_num)', data = df3).fit()
table = sm.stats.anova_lm(lmodel, type=1)
print(table)
# 해석 : PR(>F)(p_val):0.740797 > 0.05이므로 귀무채택

# 사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
result = pairwise_tukeyhsd(df3.jikwon_pay, df3.buser_num)
print(result)
result.plot_simultaneous()
plt.show()