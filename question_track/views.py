from django.shortcuts import render
from question_track.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from django.contrib.auth.models import User
from question_track.models import Question,QuestionClass,QuestionState,Solution
from question_track.forms import *
# Create your views here.
def user_login(request):
    return render(request, 'question_track/login.html')
#test
# @csrf_protect
def qms_main(request):
    questions = Question.objects.all()[0:3]
    context = {
        'questions': questions,
    }
    if request.user.is_authenticated():
        return render(request, 'question_track/home.html', context)

    state = 'None'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                return render(request, 'question_track/home.html',context)
            else:
                return render(request, 'question_track/login.html', {'state':state})
        else:
            state = '用户不存在或密码错误'
            return render(request, 'question_track/login.html', {'state':state})

    print('redirect')
    return HttpResponseRedirect('login')

def register(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect('/home')
    state=None
    registerForm=RegisterForm()
    if request.method == 'POST':
        print('post')
    content={
        'state':state,
        'registerFrom':registerForm,
    }
    print(registerForm)
    return render(request, 'question_track/register.html',content)

def project_detils():
    pass
def report():
    pass
