from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import MySQLdb


# 한글깨짐 방지
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

config = {
    'host':'127.0.0.1',
    'database':'test',
    'user':'root',
    'password':'123',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
    
    }


# Create your views here.
def mainFunc(request):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select * from jikwon"
    
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = ['직원번호', '직원명', '부서번호', '직급', '연봉', '입사일', '성별', '평가']
        
        df = pd.DataFrame(rows, columns=columns)
#         print(df)
        
        buser_sum = pd.DataFrame(df.groupby(['부서번호'])['연봉'].sum())
        buser_mean = pd.DataFrame(df.groupby(['부서번호'])['연봉'].mean())
        print(buser_sum)
        jik_sum = pd.DataFrame(df.groupby(['직급'])['연봉'].sum())
        jik_mean = pd.DataFrame(df.groupby(['직급'])['연봉'].mean())
#         buser_mean = df.pivot_table(values=['연봉'], index=['부서번호'], aggfunc=np.mean)


        x = np.arange(len(buser_mean['연봉'].values))
        plt.bar(x, buser_mean['연봉'].values)
        plt.xticks(x, buser_sum.index)
        fig = plt.gcf()
#         plt.show()
        
        fig.savefig("C:/work/Portfolio/PythonProject/pandasDjango_ex/myjikwon/static/images/mean.png")
#         print(buser_sum)

        df_html = df.to_html()
        buser_sum_html = buser_sum.to_html()
        buser_mean_html = buser_mean.to_html()
        jik_sum_html = jik_sum.to_html()
        jik_mean_html = jik_mean.to_html()
        
        cursor.close()
        conn.close()
    except Exception as e:
        print("error", e) 

        
    return render(request, 'main.html', {'datas':df_html, 'buser_sum':buser_sum_html,'buser_mean':buser_mean_html, 'jik_sum': jik_sum_html, 'jik_mean':jik_mean_html})
