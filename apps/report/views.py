from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.views.generic import View,TemplateView,ListView
from django.utils.decorators import method_decorator
# from report.forms import SigninForm
from apps.report.models import Applynew
from django.contrib.auth.models import User,Group,Permission,ContentType
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required,permission_required


# @method_decorator(login_required(login_url='/account/signin/'),name='get')
class Index(View):
    @method_decorator(login_required(login_url='/account/signin/'))
    def get(self,request):
        return render(request, 'common/index.html')


def test(request):
    return HttpResponse('testyem')


# # 个人中心,如果没有访问会被重定向到登陆的url,登录成功以后会自动跳转登录前的界面
# @login_required(login_url='/login/')
# def profile(request):
#     return HttpResponse('个人中心,登录才可以看到')
