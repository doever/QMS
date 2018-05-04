from django.shortcuts import render
from question_track.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from django.contrib.auth.models import User
from question_track.models import Question,QuestionClass,QuestionState,Solution
from question_track.forms import *
import json

# Create your views here.
class APIError(Exception):
    def __init__(self, error,data,message):
        super().__init__(self)
        self.error = error
        self.data=data
        self.message=message

    def __str__(self):
        return self.error

def api(func):
  # @functools.wraps(func)
    def _wrapper(*args, **kw):
        try:
            r = json.dumps(func(*args **kw))
            if not r:
                raise APIError('-1','data','用户不能为空')
        except APIError as e:
            r = json.dumps(dict(error=e.error, data=e.data, message=e.message))
        except Exception as e:
            r = json.dumps(dict(error='internalerror', data=e.__class__.__name__, message='服务器内部错误'))
        # ctx.response.content_type = 'application/json'
        return r
    return _wrapper

@api
def api_get_users():
  users = User.objects.raw('select * from auth_user')
  print(users)
  print(dict(users=users))
  return dict(users=users)

#######################

def get_users(request):

    response = {'status':True,'data':None,'msg':None}
    try:
        user_list = User.objects.values('id','username')
        # user_list = list(user_list),如果正确,则将user_list的数值赋值给data
        if user_list is None:
            response['msg']='null'
        response['data'] = list(user_list)
    except Exception as e:
        response['status'] = False
        response['msg'] = str(e)

    data = json.dumps(response)
    return HttpResponse(data)






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
    print('fangwenzhuce')
    if request.method == 'POST':
        print('post')
        registerForm=RegisterForm(request.post)
        if registerForm.is_valid():
            print(registerForm.cleaned_data)
            print('验证通过')
            return render(request, 'question_track/login.html')
        else:
            print('验证失败')
            print(registerForm.errors)
            return render(request, 'question_track/register.html', {"registerFrom": registerForm})
    content={
        'state':state,
        'registerFrom':registerForm,
    }
    # print(registerForm)
    return render(request, 'question_track/register.html',content)

def project_detils():
    pass
def report():
    pass
