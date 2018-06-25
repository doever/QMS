from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import connection
from .models import Question,QuestionClass,QuestionState,Solution,Applynew
from question_track.forms import *
from django.views.generic import View,ListView,TemplateView
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
import json


class Login(View):
    def get(self,request):
        if request.session.get('user_id',''):
            return redirect(reverse('question_track:index'))
        else:
            return render(request,'question_track/login.html')

    def post(self,request):
        forms = LoginForm(request.POST)
        if forms.is_valid():
            request.session['user_id'] = forms.cleaned_data.get('id')
            return redirect(reverse("question_track:index"))
        else:
            context = {
                'username':forms.cleaned_data.get('username'),
                'password':forms.cleaned_data.get('password'),
            }
            print(forms.errors)
            return render(request,'question_track/login.html',context=context)


class Register(View):
    def get(self,request):
        if request.session.get('user_id',''):
            return redirect(reverse("question_track:index"))
        else:
            return render(request,"question_track/register.html")

    def post(self,request):
        pass


class Index(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'question_track/home.html'
    paginate_by = 3
    ordering = '-createdate'

    def get_context_data(self, **kwargs):
        context = super(Index,self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Question.objects.all()


# class APIError(Exception):
#     def __init__(self, error,data,message):
#         super().__init__(self)
#         self.error = error
#         self.data=data
#         self.message=message
#
#     def __str__(self):
#         return self.error
#
# def api(func):
#   # @functools.wraps(func)
#     def _wrapper(*args, **kw):
#         try:
#             r = json.dumps(func(*args **kw))
#             if not r:
#                 raise APIError('-1','data','用户不能为空')
#         except APIError as e:
#             r = json.dumps(dict(error=e.error, data=e.data, message=e.message))
#         except Exception as e:
#             r = json.dumps(dict(error='internalerror', data=e.__class__.__name__, message='服务器内部错误'))
#         # ctx.response.content_type = 'application/json'
#         return r
#     return _wrapper
#
# @api
# def api_get_users():
#   users = User.objects.raw('select * from auth_user')
#   print(users)
#   print(dict(users=users))
#   return dict(users=users)

