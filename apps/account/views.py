#!/usr/bin/python3
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect,reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views import View
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate,logout,login
# from .models import User
from .forms import LoginForm
from django.contrib.auth import get_user_model
from apps import restful

User = get_user_model()


def add_user(request):
    username='chenlong'
    password='111111'
    telephone='11012341234'
    email = '1234@qq.com'
    User.objects.create_user(username=username,password=password,telephone=telephone,email=email)
    return HttpResponse('成功创建用户')

class Signin(View):
    def get(self,request):
        return render(request,'account/login.html')

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            print(username)
            print(password)
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    if remember:
                        request.session.set_expiry(None)
                    else:
                        request.session.set_expiry(0)
                    login(request, user)
                    return restful.ok()
                    # return redirect(reverse("report:index"))
                else:
                    return restful.unauth(message="用户已被停用")
            else:
                return restful.params_error(message="用户不存在或密码错误")
        else:
            print(form.get_errors())
            return restful.params_error(message=form.get_errors())


def list_view(request):
    # user = User.objects.all()
    user = ['1','2','3','4']
    paginator = Paginator(user,10)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return HttpResponse('123')


class UserView(View):
    def get(self,request):
        users = User.objects.all()
        return render(request,"account/user.html",context={'users':users})

    def put(self,request):
        pass

    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        email = request.POST.get('email','')
        telephone = request.POST.get('telephone','')
        image = request.FILES.get('image')
        user = User.objects.create_user(username=username,password=password,email=email,telephone=telephone,image=image)
        return restful.ok()

    def delete(self,request):
        pass


def gettemplates(request,templates):
    print(templates)
    return render(request,"account/%s" % templates)