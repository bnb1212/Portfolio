from django.shortcuts import render
from jikwons.models import Jikwon, Gogek, Buser
import datetime


# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def errorFunc(request):
    return render(request, 'error.html')

def jikwonFunc(request):
    try:
        gogek_data = Gogek.objects.get(gogek_name=request.POST.get('inp_gogek_name'), gogek_tel=request.POST.get('inp_gogek_tel'))

    except Exception:
        return render(request, 'error.html')
    
    # gogek_data.gogek_damsano는 jikwon Object이다. 외래키이기 떄문에?
    jikwon_data = gogek_data.gogek_damsano

    # 부서 데이터 획득 ====================
    # get 반환 객체에 접근 할때는 . 으로 접근 (dot notation)
    buser_num = jikwon_data.buser_num
    
    buser_data = Buser.objects.get(buser_no=buser_num)
    # ======================================

    # 근무 년수 획득 ========================
    gundays = datetime.date.today() - jikwon_data.jikwon_ibsail
    
#     print(gundays)
    gunyears = gundays.days // 365
#     print(gunyears)
    # =========================================
    
    
    # 고객 평점 연산 ==========================
    if jikwon_data.jikwon_rating == 'a':
        jik_grade = "최우수"
    elif jikwon_data.jikwon_rating == 'b':
        jik_grade = "우수"
    else:
        jik_grade = "일반"
    # =========================================
        
    
    return render(request, 'jikwon.html', {'jikwon':jikwon_data, 'buser':buser_data, 'gunyears':gunyears, 'jik_grade':jik_grade})

