''' ===================================
[ANOVA 예제 1]

빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.
======================================== '''
# 귀무 : 빵을 귀름에 튀길때 기름의 종류에 따라 빵에 흡수된 기름의 양에 차이가 없다.
# 대립 : 빵을 귀름에 튀길때 기름의 종류에 따라 빵에 흡수된 기름의 양에 차이가 있다.

import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import MySQLdb

# 데이터 프레임 만들기
k_list = [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2]
df1 = pd.DataFrame(k_list,columns=['kind'])
df1['quantity'] = [64, 72, 68, 77, 56, None, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]
df1 = df1.fillna(df1.mean())
print(df1.head(3))

# 종류별 그룹 만들어 정규성 검사
group1 = df1[df1['kind'] == 1]['quantity']
g_list1 = list(group1)
# print(group1)
# print(g_list1)
group2 = df1[df1['kind'] == 2]['quantity']
group3 = df1[df1['kind'] == 3]['quantity']
group4 = df1[df1['kind'] == 4]['quantity']

print(stats.shapiro(group1))
print(stats.shapiro(group2))
print(stats.shapiro(group3))
print(stats.shapiro(group4)) # 모두 정규성을 만족한다.//

# 그룹들의 등분산성 검정
print(stats.levene(group1, group2, group3, group4).pvalue) # p_value > 0.05 등분산성 만족//

# 그룹간 데이터들의 분포를 시각화
# plot_data = [group1, group2, group3, group4]
# plt.boxplot(plot_data)
# plt.show()

f_statistic, p_val = stats.f_oneway(group1, group2, group3, group4)
print('일원분산분석 결과 : f_statistic:%f, p_val:%f'%(f_statistic, p_val))
# p_val : 0.84 이므로 0.05보다 크다. 귀무가설을 채택한다. 
# 빵을 귀름에 튀길때 기름의 종류에 따라 빵에 흡수된 기름의 양에 차이가 없다는 의견이 통계적으로 유의하다.

print("\n --------------------------------------------------------------------------------------------\n")
''' ================================
[ANOVA 예제 2]

DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
====================================''' 

# 귀무 : 각 부서별 연봉 평균에 차이가 없다.
# 대립 : 각 부서별 연봉 평균에 차이가 있다.

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

sql = "select jikwon_no, jikwon_name, jikwon_jik, jikwon_pay, buser_name from jikwon left outer join buser on buser_no = buser_num"

df2 = pd.read_sql(sql, conn)

# 종류별 그룹 만들어 정규성 검사
group1 = df2[df2['buser_name'] == '총무부']['jikwon_pay']
g_list1 = list(group1)
# print(group1)
# print(g_list1)
group2 = df2[df2['buser_name'] == '영업부']['jikwon_pay']
group3 = df2[df2['buser_name'] == '전산부']['jikwon_pay']
group4 = df2[df2['buser_name'] == '관리부']['jikwon_pay']

print(stats.shapiro(group1)) # 정규성 만족 X
print(stats.shapiro(group2)) # 정규성 만족 X
print(stats.shapiro(group3)) # 정규성 만족 O
print(stats.shapiro(group4)) # 정규성 만족 O

# 그룹간 데이터들의 분포를 시각화
# plot_data = [group1, group2, group3, group4]
# plt.boxplot(plot_data)
# plt.show()

# 일원 분산 분석 방법
# f_statistic, p_val = stats.f_oneway(group1, group2, group3, group4)
# print('일원분산분석 결과 : f_statistic:%f, p_val:%f'%(f_statistic, p_val))
# p_val : 0.745 이므로 0.05보다 크다. 귀무가설을 채택한다. 
# 각 부서별 연봉 평균에 차이가 없다는 의견이 통계적으로 유의하다.

# 정규성을 따르지 않는 그룹이 2개 있으므로 kruskal-Wallis Test를 이용한다.
h_statistic, p_val = stats.kruskal(group1, group2, group3, group4)
print('일원분산분석 결과 : h_statistic:%f, p_val:%f'%(h_statistic, p_val))
# p_val : 0.643344 이므로 0.05보다 크다. 귀무가설을 채택한다. 
# 각 부서별 연봉 평균에 차이가 없다는 의견이 통계적으로 유의하다.