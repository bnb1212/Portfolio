
# 문제1 ----------------------------------------------------------------
# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.

# 귀무 : 포장지 색상에 따른 제품의 매출액에 차이가 없다.
# 대립 : 포장지 색상에 따른 제품의 매출액에 차이가 있다.

import numpy as np
import scipy as sp
import scipy.stats as stats
import random
import MySQLdb
print('문1)')
blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

# 정규성 확인
print(stats.shapiro(blue)) # 0.510 > 0.05이므로 정규성 분포를 이룸
print(stats.shapiro(red)) # 0.534 > 0.05이므로 정규성 분포를 이룸
# print(stats.wilcoxon(blue))
print(stats.ttest_ind(blue, red, equal_var=True))

# Ttest_indResult(statistic=2.9280203225212174, pvalue=0.008316545714784403)
# 해석 : pvalue=0.0083 < 0.05이므로 귀무가설 기각. 차이가 있다.
print("\n-------------------------------------------------------------\n")
# ------------------------------------------------------------------------
 
# [two-sample t 검정 : 문제2]  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.

# 귀무 : 남녀 간에 혈관 내의 콜레스테롤 양에 차이가 없다. 
# 대립 : 남녀 간에 혈관 내의 콜레스테롤 양에 차이가 있다. 
print('문2)')
male = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]
random.seed(20)

male_sample = random.sample(male, 15)
female_sample = random.sample(female, 15)

import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot(male, kde=True, fit=stats.norm) 
# sns.distplot(female, kde=True, fit=stats.norm)
# plt.show() 

print(stats.shapiro(male_sample)) # pvalue : 0.0052
print(stats.shapiro(female_sample)) # pvalue : 0.00075 
# print(stats.wilcoxon(female_sample))

# 등 분산성
print(stats.levene(male_sample, female_sample).pvalue) # p_value > 0.05

# 정규성을 만족하지 않으므로 man-whitney 검정
print(stats.mannwhitneyu(male_sample, female_sample))

# print(stats.ttest_ind(male_sample, female_sample, equal_var = True)) # 등분산성을 만족한 경우
# Ttest_indResult(statistic=-0.6266360256307733, pvalue=0.5359739459567937) - seed(21) 차이가 없다
# pvalue 0.3778 > 0.05 귀무가설 채택. 차이가 없다. 
print("\n-------------------------------------------------------------\n")
# ----------------------------------------------------------------------------
# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
print('문3)')
import pandas as pd
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

df = pd.read_sql(sql, conn)
# print(df)

chongmu = df[df['buser_name'] == '총무부']
youngup = df[df['buser_name'] == '영업부']
# print(type(chongmu))

c_pay = chongmu['jikwon_pay']
y_pay = youngup['jikwon_pay']
# print(c_pay)
c_pay = c_pay.fillna(c_pay.mean())
y_pay = y_pay.fillna(y_pay.mean())

print(stats.shapiro(c_pay)) # 0.026 < 0.05이므로 정규성 분포를 이루지 않음
print(stats.shapiro(y_pay)) # 0.025 < 0.05이므로 정규성 분포를 이루지 않음
print(stats.levene(c_pay, y_pay).pvalue) # 0.91 > 0.05 이므로 등분산성


# 정규성을 만족하지 않음
print(stats.mannwhitneyu(c_pay, y_pay))
# MannwhitneyuResult(statistic=33.0, pvalue=0.23606673040062592)
# 해석 : p-value : 0.23 > 0.05이므로 연봉 평균에는 차이가 없다. 귀무가설 채택

# print(stats.ttest_ind(c_pay, y_pay, equal_var = True)) 
# Ttest_indResult(statistic=0.4585177708256519, pvalue=0.6523879191675446)
# 해석 : p-value ; 0.652 > 0.05 이므로 연봉평균에는 차이가 없다. 귀무가설 채택
print("\n-------------------------------------------------------------\n")

# ------------------------------------------------------------------------------------------

# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

# 귀무 : 학급의 학업능력엔 변화가 없다
# 귀무 : 학급의 학업능력엔 변화가 있다
print('문4)')
middle = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
final = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print(stats.shapiro(middle)) 
print(stats.shapiro(final))

print(stats.ttest_rel(middle, final))
# Ttest_relResult(statistic=-2.6281127723493993, pvalue=0.023486192540203194)
# 해석 : p-value : 0.023 < 0.05 이므로 귀무가설 기각. 학업능력에 변화가 있다.
