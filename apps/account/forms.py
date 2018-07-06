#!/usr/bin/python3
import re

from django import forms
from django.db.models import Q

# 简化message提取
from apps.forms import FormMixin
from .models import User


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


class UserManageForm(forms.ModelForm,FormMixin):
    # telephone = forms.CharField(validators=[validators.RegexValidator(r'1\d{10}', message="请输入正确的手机号码！！！")])
    class Meta:
        model = User
        fields = ['username','nickname','telephone','password','email','image','birday','work_position']
        error_messages = {
            "username":{
                "required":"请输入用户名",
                "max_length":"用户名超出长度",
                "invalid": "请输入有效的用户名",
            },
            "nickname": {
                "required": "请输入用户名",
                "max_length": "用户名超出长度",
                "invalid": "请输入有效的用户名",
            },
            "telephone": {
                "required": "请输入手机号码",
                "max_length": "请输入有效的手机号码",
                "invalid": "请输入有效的手机号码",
            },
            "password": {
                "required": "请输入密码",
                "max_length": "密码超出长度",
                "invalid": "请输入有效的参数",
            },
            "email": {
                "required": "请输入邮箱",
                "max_length": "邮箱超出长度",
                "invalid": "请输入有效的邮箱",
            },
            "birday": {
                "invalid": "请输入有效的生日",
            }
        }

    def clean(self):
        cleaned_data = super(UserManageForm, self).clean()
        username = cleaned_data.get('username')
        telephone = cleaned_data.get('telephone')
        email = cleaned_data.get('email')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(message="用户名已存在")

        if User.objects.filter(Q(telephone=telephone)|Q(email=email)).exists():
            raise forms.ValidationError(message="手机或邮箱已存在")

        if not re.search('1[3-9]\d{9}', str(telephone)) or len(str(telephone)) != 11:
            raise forms.ValidationError(message="您输入的手机有误")

        return cleaned_data


