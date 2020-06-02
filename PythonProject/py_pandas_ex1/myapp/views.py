from django.shortcuts import render
import MySQLdb
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
# Create your views here.


def Main(request):
    return render(request, 'Main.html')


def Jikwon(request):
    
    config = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'123',
        'database':'test',
        'port':3306,
        'charset':'utf8',
        'use_unicode':True
    }
    
    try:
        sql = "select * from jikwon join buser on buser_no = buser_num"
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()  
        df = pd.read_sql(sql, conn)
        
        print(df.head(5))
        
        jikwon_bpay_sum = df.groupby(['buser_name'])['jikwon_pay'].sum()
        jikwon_bpay_mean = df.groupby(['buser_name'])['jikwon_pay'].mean()
        jikwon_jpay_sum = df.groupby(['jikwon_jik'])['jikwon_pay'].sum()
        jikwon_jpay_mean = df.groupby(['jikwon_jik'])['jikwon_pay'].mean()
        
        print(jikwon_bpay_sum)
        print(jikwon_bpay_mean)
        print(jikwon_jpay_sum)
        print(jikwon_jpay_mean)
        
        plt.rc('font', family='malgun gothic')
        plt.rcParams['axes.unicode_minus'] = False
        
        fig = plt.figure()  # 차트 영역에 대한 객체선언
        
        ax1 = fig.add_subplot(3, 3, 1)
        ax2 = fig.add_subplot(3, 3, 3)
        ax3 = fig.add_subplot(3, 3, 7)
        ax4 = fig.add_subplot(3, 3, 9)
        
        ax1.bar(jikwon_bpay_sum.index, jikwon_bpay_sum, color='red')
        ax2.bar(jikwon_bpay_mean.index, jikwon_bpay_mean, color='green')
        ax3.bar(jikwon_jpay_sum.index, jikwon_jpay_sum, color='blue')
        ax4.bar(jikwon_jpay_mean.index, jikwon_jpay_mean, color='yellow')
        
        ax1.title.set_text('부서별 급여합')
        ax2.title.set_text('부서별 급여평균')
        ax3.title.set_text('직급별 급여합')
        ax4.title.set_text('직급별 급여평균')
        
        image_location = '../static/images/jikwon.png'
        
        plt.gcf().savefig('C:\py_sou\py_pandas_ex1\myapp\static\images\jikwon.png')
        
    except Exception as e:
        print('에러', e)
    
    return render(request, 'jikwon.html', {'image':image_location})
