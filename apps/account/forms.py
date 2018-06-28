#!/usr/bin/python3
from django import forms
# 简化message提取
from apps.forms import FormMixin

class LoginForm(forms.Form,FormMixin):
    username = forms.CharField(max_length=20,error_messages={
        'max_length':'用户名超出限制',
        'required':'请输入用户名'
    })
    password = forms.CharField(max_length=16,error_messages={
        'max_length':'密码过长',
        'required':'请输入密码'
    })
    remember = forms.BooleanField(required=False)




