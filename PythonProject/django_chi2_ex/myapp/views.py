from django.shortcuts import render
from myapp.models import Survey
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots


# Create your views here.

def mainFunc(request):
    return render(request, 'main.html')

def surveyEnterFunc(request):
    return render(request, 'survey.html')

def surveyProcessFunc(request):
    #신규 자료 저장
    insertData(request)
    rdata = list(Survey.objects.all().values())
    df, crossTab, results = chiFunc(rdata)

    # 시각화: 커피사별 선호 건수
    
    # 한글깨짐 방지
    plt.rc('font', family='malgun gothic')
    plt.rcParams['axes.unicode_minus'] = False


    fig = plt.gcf()
    co_group = df['co_survey'].groupby(df['coNum']).count()
    print(co_group)
    co_group.plot.bar(subplots= True, color=['lightblue', 'pink'], width=0.5)
    plt.xlabel('커피사')
    plt.ylabel('선호건수')
    plt.title('커피사 별 선호 건수')
    fig.savefig('django_chi2_ex/myapp/static/images/vbar.png')
    
    return render(request, 'list.html', {'df':df.to_html(classes='table table-bordered'), 'crossTab':crossTab.to_html(classes='table table-bordered'), 'results':results})

def insertData(request):
#     print(request.POST.get('gender'))
#     print(request.POST.get('age'))
#     print(request.POST.get('coffeebrand'))
    if request.method =="POST":
        Survey(
            # rnum = len(list(Survey.objects.all().values())) + 1 # 자동 증가 칼럼이 아니라면 직접 증가시킨다.
            gender = request.POST.get('gender'),
            age = request.POST.get('age'),
            co_survey = request.POST.get('coffeebrand'),
        ).save()
    
import pandas as pd
import scipy.stats as stats
def chiFunc(rdata):
#     print(rdata, ' ', type(rdata))
    df = pd.DataFrame(rdata)
    df.dropna()
    # 성별 1, 2로 저장
    df['genNum'] = df['gender'].apply(lambda g:1 if g =='남' else 2)
    # 선호 브랜드 1,2,3,4로 저장
    df['coNum'] = df['co_survey'].apply(lambda c:1 if c == '스타벅스' else 2 if c == '커피빈' else 3 if c == '이디야' else 4)
#     print(df)
    
    crossTab = pd.crosstab(index=df['genNum'], columns=df['coNum'])
#     print(crossTab)
    
    st, pv, _, _ = stats.chi2_contingency(crossTab)
    print(pv)
    if pv >= 0.05:
        results = 'p값이 {0:.8} : 0.05 이상이므로 0.05 <br>성별에 따른 선호 커피 브랜드에는 차이가 없다(귀무).'.format(pv)
#         print(results)
    else:
        results = 'p값이 {0:.8} : 0.05 미만이므로 0.05 <br>성별에 따른 선호 커피 브랜드에는 차이가 있다(대립).'.format(pv)
        
    return df, crossTab, results
    
    
    
    