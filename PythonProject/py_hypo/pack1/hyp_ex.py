# * 이원카이제곱 검정 ( 카이제곱 독립 검정 )
# 
# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 : NA가 있는 행은 제외한다.
# 
# 카이제곱 문제2) jikwon_jik과 jikwon_pay 간의 관련성 분석. 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.

import pandas as pd
import scipy.stats as stats
import MySQLdb

# ------------------------------------------------------------------------------------
# 귀무가설 : 부모의 학력 수준과 자녀의 대학 진학 여부는 관련이 없다. (독립적이다)
# 대립가설 : 부모의 학력 수준과 자녀의 대학 진학 여부는 관련이 있다. (독립적이지 않다 = 연관이 있다.)

data1 = pd.read_csv('../testdata/cleanDescriptive.csv')
# print(data1['pass'].head())
# print(data1.columns)
data1 = data1.dropna()

ctab = pd.crosstab(index=data1['level'], columns=data1['pass'])
ctab.index = ['고졸', '대졸', '대학원졸']
ctab.columns = ['합격', '실패'] 
print(ctab)
 
# chi_result = [ctab.loc['대학원졸'],ctab.loc['대졸'],ctab.loc['고졸']]
chi2, p, df, _ = stats.chi2_contingency(ctab)
print(chi2, p, df)

# 해석 : p:0.02 < 0.05 이므로 귀무가설 기각. 관련이 있다.

print('\n-------------------------------------------------\n')

# 귀무가설 : 직원의 직급과 연봉은 관련이 없다. (독립적이다)
# 대립가설 : 직원의 직급과 연봉은 관련이 있다. (독립적이지 않다)

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

sql = "select jikwon_no, jikwon_name, jikwon_jik, jikwon_pay from jikwon"

data2 = pd.read_sql(sql, conn)
data2 = data2.dropna()
print(data2)

bins = [1000, 3000, 5000, 7000, 10000]
labels = [1, 2, 3, 4]
data2["jikwon_pay"] = pd.cut(data2['jikwon_pay'], bins, labels=labels)
# print(data2)

data2 = data2.replace({'이사':1, '부장':2, '과장':3, '대리':4, '사원':5})

ctab2 = pd.crosstab(index=data2['jikwon_jik'], columns=data2['jikwon_pay'])
# ctab2.index= ['이사', '부장', '과장', '대리', '사원']
print(ctab2)

chi2, p, df, _ = stats.chi2_contingency(ctab2)
print(chi2, p, df)
print("p:0.00029 < 0.05 이므로 귀무가설 기각. 관련이 있다.")

# 해석 : p:0.00029 < 0.05 이므로 귀무가설 기각. 관련이 있다.
