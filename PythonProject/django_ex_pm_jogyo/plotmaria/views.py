from django.shortcuts import render
import pandas as pd
import numpy as np
from plotmaria.models import Jikwon, Buser
import matplotlib.pyplot as plt 
plt.rc('font',family='Malgun gothic') #matplotlib쓸때 위아래 다 세트. 한글이라서.
plt.rcParams['axes.unicode_minus'] = False

# Create your views here.
def Main(request):
    return render(request,'main.html')
    
def List(request):
    jdata = Jikwon.objects.all()
    bdata = Buser.objects.all()
    
    jno = []
    jname = []
    bb = []
    jjik = []
    jpay = []
    
    for j in jdata:
        bn=''
        for b in bdata:
            if j.buser_num == b.buser_no:
                bn = b.buser_name 
        
        jno.append(j.jikwon_no)
        jname.append(j.jikwon_name)
        bb.append(bn)
        jjik.append(j.jikwon_jik)
        jpay.append(j.jikwon_pay)
    
    dicData = {'번호':jno,'이름':jname,'부서':bb,'직급':jjik,'연봉':jpay}
    df = pd.DataFrame(dicData)
    #print(df)
    
    js = df.groupby(['직급'])['연봉'].sum().astype(int) #직급별 급여합
    print(js)
    plt.bar(js.index,js.values)
    
    fig = plt.gcf() #차트를 이미지로 저장 준비
    fig.savefig('C:\work\py_sou\django_ex_pm\plotmaria\static\img\js.png')
    plt.cla()
    js = pd.DataFrame(js)
     
    jm = df.groupby(['직급'])['연봉'].mean().astype(int) #직급별 급여평균
    print(jm)
    plt.bar(jm.index,jm.values)
    fig = plt.gcf() #차트를 이미지로 저장 준비
    fig.savefig('C:\work\py_sou\django_ex_pm\plotmaria\static\img\jm.png')
    plt.cla()
    jm = pd.DataFrame(jm)
     
    bs = df.groupby(['부서'])['연봉'].sum().astype(int) #부서별 급여합
    print(bs)
    plt.bar(bs.index,bs.values)
    fig = plt.gcf() #차트를 이미지로 저장 준비
    fig.savefig('C:/work/py_sou/django_ex_pm/plotmaria/static/img/bs.png')
    plt.cla()
    bs = pd.DataFrame(bs) 
     
    bm = df.groupby(['부서'])['연봉'].mean().astype(int) #부서별 급여평균
    print(bm)
    plt.bar(bm.index,bm.values)
    fig = plt.gcf() #차트를 이미지로 저장 준비
    fig.savefig('C:/work/py_sou/django_ex_pm/plotmaria/static/img/bm.png')
    plt.cla()
    bm = pd.DataFrame(bm)
    
    return render(request,'list.html',
                  {'datas':js.to_html(),'datas2':jm.to_html(),'datas3':bs.to_html(),'datas4':bm.to_html()})
