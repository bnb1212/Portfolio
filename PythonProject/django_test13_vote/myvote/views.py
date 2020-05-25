from django.shortcuts import render, get_object_or_404
from myvote.models import Question, Choice
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls.base import reverse


# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')


def DispFunc(request):
    q_list = Question.objects.all().order_by('pub_date', 'id')
    context = {'q_list':q_list}
    
    return render(request, 'display.html', context)

def DetailFunc(request, question_id):  # /gogo/1
    # return HttpResponse('question_id : %s' % question_id)
    
    
    # 이놈들은 한줄에 쓸 수 있다!======================
#     try:
#         question = Question.objects.get(pk=question_id)
#         
#     except Question.DoesNotExist:
#         # 에러 던지기
#         raise Http404("Question 자료가 없습니다!")
    # =================================================
    
    #                ||
    #                ||
    #                ||
    #                \ /
    #                 V
    question = get_object_or_404(Question, pk=question_id)
    
    
    
    print(question.question_text)
    print(question.pub_date)
    
    return render(request, 'detail.html', {'question' : question})

def VoteFunc(request, question_id):  # /gogo/1
    question = get_object_or_404(Question, pk=question_id)
                                 
    try:
        sel_choice = question.choice_set.get(pk=request.POST['choice'])
        
    # 선택 항목이 없을때 
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question' : question, 'error_msg' : '투표 1개 항목을 선택하세요'})
        
    # 투표항목 1 누적후 갱신
    sel_choice.votes += 1
    sel_choice.save()    
    
    # print(reverse('results', args=(question.id, )))
    return HttpResponseRedirect(reverse('results', args=(question.id, )))
    


def ResultFunc(request, question_id):  # /gogo/1
#     return HttpResponse('result of question : %s' % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question':question})
    
    
