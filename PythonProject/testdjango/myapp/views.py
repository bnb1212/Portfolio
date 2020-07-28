from django.shortcuts import render

# Create your views here.
def helloFunc(request):
    a = 10
    b = 20
    c = a + b
    
    return render(request, 'hellodjango.html', {'result':c})

def wowFunc(request):
    return render(request, 'wow.html')

def indexFunc(request):
    return render(request, 'index.html')