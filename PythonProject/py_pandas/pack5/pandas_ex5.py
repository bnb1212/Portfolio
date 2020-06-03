import MySQLdb
import pandas as pd
import numpy as np

config = {  # dictionary 타입
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

conn = MySQLdb.connect(**config)

sql = """
select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_pay
from jikwon inner join buser
on buser_num = buser_no
"""

df = pd.read_sql(sql, conn)

buser_sum = df.groupby(['buser_name'])['jikwon_pay'].sum()
buser_mean = df.groupby(['buser_name'])['jikwon_pay'].mean()

print('------연봉 합------')
print(buser_sum)
print()
print('------연봉 평균----')
print(buser_mean)

crx_tab1 = pd.crosstab(df.buser_name, df.jikwon_jik, rownames = ['부서명'], colnames=['직급'], margins=True)
print(crx_tab1)

sql = """
select jikwon_name, gogek_name, gogek_no from jikwon inner join gogek on jikwon_no = gogek_damsano
"""

df2 = pd.read_sql(sql, conn)
print(df2)
df2 = df2.sort_values('jikwon_name')
df2 = df2.set_index(['jikwon_name', 'gogek_no'])

print(df2)

df2.to_excel('./pandas_ex.xlsx')
