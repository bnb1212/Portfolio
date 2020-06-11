from django.shortcuts import render
from mysurvey.models import Surveydata
# django_pandas 모듈 설치
from django_pandas.io import read_frame
import scipy.stats as stats
import matplotlib.pyplot as plt
import os
import seaborn as sns


# Create your views here.
def indexFunc(request):
    return render(request, 'index.html')
    plt.cla()


def surveymainFunc(request):
    return render(request, 'surveymain.html')


def surveyProcessFunc(request):
    insertData(request)
    t_result = tTestFunc()
    f_result = oneWayAnovaFunc()
    return render(request, 'chartmain.html', {'t_result':t_result, 'f_result':f_result})


def insertData(request):
    if request.method == "POST":
        try:
            Surveydata(
                job=request.POST.get('job'),
                gender=request.POST.get('gender'),
                game_time=request.POST.get('game_time'),
            ).save()
        except Exception as e:
            print('저장실패', str(e))
            
    
# 성별 t_test        
def tTestFunc():
    data_qs = Surveydata.objects.all()
    data_df = read_frame(data_qs)
#     print(data_df)

    female_gtime = data_df[data_df['gender'] == '여']['game_time']
    print(female_gtime)
    male_gtime = data_df[data_df['gender'] == '남']['game_time']
    
    # == 정규성검사 ==
#     print(stats.shapiro(female_gtime))
#     print(stats.shapiro(male_gtime))
    
    genderGraph(data_df)
    t_result = stats.ttest_ind(female_gtime, male_gtime)
    print(type(t_result[1]))
    
    str_result = "p-value는 {0:.6f}".format(t_result[1])
    print(str_result)
    if t_result[1] < 0.05:
        str_result += "으로 남녀 평균 게임시간 차이가 난다는 가설은 통계적으로 유의합니다."
    else:
        str_result += "으로 남녀 평균 게임시간 차이가 난다는 가설은 통계적으로 유의하지않습니다."
    return str_result

    
# 직업 one-way anova 
def oneWayAnovaFunc():
    data_qs = Surveydata.objects.all()
    data_df = read_frame(data_qs)
    
    white_gtime = data_df[data_df['job'] == '화이트칼라']['game_time']
    blue_gtime = data_df[data_df['job'] == '블루칼라']['game_time']
    student_gtime = data_df[data_df['job'] == '학생']['game_time']
    etc_gtime = data_df[data_df['job'] == '기타']['game_time']
    
    # 평균값들
    data = [white_gtime.mean(), blue_gtime.mean(), student_gtime.mean(), etc_gtime.mean()]
    labels = ['화이트칼라', '블루칼라', '학생', '기타']
    
    # 그래프그리기 함수호출
    jobGraph(data, labels)
    
    # one-way 검정
    f_result = stats.f_oneway(white_gtime, blue_gtime, student_gtime, etc_gtime)
    str_result = "p-value는 {0:.6f}"
    if f_result[1] < 0.05:
        str_result += "으로 직업 평균 게임시간 차이가 난다는 가설은 통계적으로 유의합니다."
    else:
        str_result += "으로 직업 평균 게임시간 차이가 난다는 가설은 통계적으로 유의하지않습니다."
    return str_result.format(f_result[1])

    
# 성별 그래프
def genderGraph(data_df):
    # == 시각화 ==
    # 한글깨짐 방지
    plt.rc('font', family='malgun gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams["figure.figsize"] = (5,5)
    
    # 그래프 그리기 (seaborn)
    gender_graph = sns.barplot(
        data=data_df,
        x="gender",
        y="game_time",     
        linewidth = 5
        )
    
    
    gender_graph.set(xlabel='성별', ylabel='평균 게임시간')

    # 그래프 그리기 (matplot)
#     data_df = data_df.groupby(['gender']).mean()['game_time']
#     data_df.plot(kind='bar')
    plt.savefig(os.path.dirname(os.path.realpath(__file__)) + '\\static\\images\\gen_mean_chart.png')
    plt.close()
    
        # == 시각화 ==
def jobGraph(data, labels):
    # 한글깨짐 방지
    plt.rc('font', family='malgun gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams["figure.figsize"] = (5,5)
    
    # 그래프 그리기
    
    plt.pie(data, shadow=True, labels=labels, autopct="%1.1f%%")
    plt.savefig(os.path.dirname(os.path.realpath(__file__)) + '\\static\\images\\job_mean_chart.png')
    plt.close()
