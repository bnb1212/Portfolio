from django.shortcuts import render
from myapp.models import Profile


# Create your views here.
def Index(request):
    return render(request, 'index.html')


def Calldict(request):
    # DB에서 읽어오기
    profile_data = Profile.objects.all()
    # print(profile_data)
    pro_list = []
    
    # DB에 읽어온 데이터를 리스트에 저장
    for pro in profile_data:
        pro_dict = {}
        pro_dict['name'] = pro.name
        pro_dict['age'] = pro.age
        pro_list.append(pro_dict)
    
#     print(pro_list)

    # 데이터가 저장된 리스트를 context에 저장
    context = {'dictdata':pro_list}
    
    return render(request, 'list.html', context) 
    
