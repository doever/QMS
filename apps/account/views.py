#!/usr/bin/python3
import os

from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.views import View
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate,logout,login
from django.conf import settings
from django.http import QueryDict
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# from .models import User
from .forms import LoginForm,UserManageForm
from django.contrib.auth import get_user_model
from apps import restful


User = get_user_model()


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


# @require_POST
def logout_view(request):
    logout(request)
    return redirect(reverse("account:signin"))


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


# 用户管理视图
@method_decorator(login_required(login_url='/account/signin/'),name='get')
class UserView(View):
    def get(self,request):
        users = User.objects.filter(is_active=1)
        paginator = Paginator(users,10)
        page = request.GET.get('page')
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        return render(request,"account/user.html",context={'users':users,'paginator':paginator})

    def put(self,request):
        qd = QueryDict(request.body)
        put_dict = {k: v[0] if len(v) == 1 else v for k, v in qd.lists()}
        user_id = put_dict.get('userid','')
        user_name = put_dict.get('username','')
        password = put_dict.get('password','')
        telephone = put_dict.get('telephone','')
        email = put_dict.get('email','')
        user = User.objects.filter(pk=user_id).update(username=user_name,telephone=telephone,email=email)
        return restful.ok()

    def post(self,request):
        form = UserManageForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            # username = request.POST.get('username','')
            # password = request.POST.get('password','')
            # email = request.POST.get('email','')
            # telephone = request.POST.get('telephone','')
            # image = request.POST.get('user-img','')
            # birday = request.POST.get('birday','')
            # user = User.objects.create_user(username=username,password=password,email=email,telephone=telephone,image=image,birday=birday)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_first_error())

    def delete(self,request):
        qd = QueryDict(request.body)
        delete_dict = {k: v[0] if len(v) == 1 else v for k, v in qd.lists()}
        user_id = delete_dict.get('user_id','')
        user = User.objects.get(pk=user_id)
        user.is_active = False
        user.save()
        return restful.ok()


def user_edit(request,user_id):
    user = User.objects.get(pk=user_id)
    return render(request,"account/user_edit.html",context={'user':user})


# 处理用户上传头像路径
@require_POST
def save_img(request):
    file = request.FILES.get('file')
    name = file.name
    position = 'userhead/'+name
    print(position)
    with open(os.path.join(settings.MEDIA_ROOT,position), 'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    return restful.ok(data={'url':position})


# 用于layer返回模板
def gettemplates(request,templates):
    return render(request,"account/%s" % templates)

