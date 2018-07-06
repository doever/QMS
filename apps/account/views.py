#!/usr/bin/python3
import os
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.views import View
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from django.http import QueryDict
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q,F
from django.core.cache import cache
from django_redis import get_redis_connection

# from .models import User
from .forms import LoginForm,UserManageForm
from django.contrib.auth import get_user_model
from apps import restful
from apps.utils.email_send import send_reset_email
from apps.utils.captcha.ozcaptcha import Captcha

User = get_user_model()
de_redis_conn = get_redis_connection("default")


class AuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(telephone=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


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
        users = User.objects.filter(is_active=1).order_by("-data_joined")
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
            user.image = request.POST.get("image")
            user.set_password(password)
            user.save()
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


# 处理用户上传头像
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


class ForgetView(View):
    def get(self,request):
        return render(request,"account/forget.html")

    def post(self,request):
        email = request.POST.get('email')
        captcha_code = request.POST.get('imgcode')
        if email:
            cache_code = cache.get(captcha_code)
            if captcha_code.lower() == cache_code:
                send_reset_email(email=email)
                # 传入email用于回传
                return restful.ok(message=email)
            else:
                return restful.params_error(message="验证码错误")
        else:
            return restful.params_error(message="请填写邮箱")


class ResetView(View):
    def get(self,request):
        return render(request,"account/reset_password.html")

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        vaild_code = request.POST.get('vaild_code')
        cache_code = cache.get(email)
        if de_redis_conn.llen(email+'error') >= 5:
            # from django.shortcuts import render_to_response
            # response = render_to_response('403.html', {})
            # response.status_code = 403
            # return response
            return restful.forbidden_error(message='访问频繁')

        if password != re_password:
            return restful.params_error('两次密码不一致')
        if vaild_code != cache_code:
            # 限制用户频繁输入错的验证码
            bad_key = email+'error'
            de_redis_conn.lpush(bad_key,1)
            return restful.params_error('验证码错误')

        user = User.objects.get(email=email)
        if user:
            user.set_password(password)
            user.save()
            return restful.ok()
        else:
            return restful.params_error(message="用户不存在")


def img_captcha(request):
    text,image = Captcha().gene_code()
    out = BytesIO()
    image.save(out,'png')
    out.seek(0)
    cache.set(text.lower(),text.lower(),5*60)
    response = HttpResponse(content_type='image/png')
    response.write(out.read())
    response['Content-length'] = out.tell()
    return response






