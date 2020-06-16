from django.shortcuts import render
'''======================================
회귀분석 문제 3) 
원격 DB의 jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성하시오.
장고로 작성한 웹에서 근무년수를 입력하면 예상연봉이 나올 수 있도록 프로그래밍 하시오.
======================================'''
# Create your views here.
from myjikwon.models import Jikwon
from django_pandas.io import read_frame 
from datetime import datetime
from django.db.models.functions.text import Substr
import pandas as pd

def mainFunc(request):
    return render(request, 'main.html')

def jikwonRegFunc(request):
    input_year = request.GET.get('g_year')
    print(input_year)
    qs = Jikwon.objects.all().annotate(ibsail_year=Substr('jikwon_ibsail',1,4)).values('ibsail_year', 'jikwon_pay')
    df = read_frame(qs)
    df['ibsail_year'] = pd.to_numeric(df['ibsail_year'])
#     print(df)
    now_year = datetime.today().year
    print(now_year, type(now_year))
    
    df['ibsail_year'] = now_year - df['ibsail_year'] 
     
    print(df)
    return render(request, 'result.html', {'data':df.to_html(classes='table table-bordered')})