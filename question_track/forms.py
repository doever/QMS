#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

# class RegisterForm(forms.Form):
#     username = forms.CharField(
#         label=u'用户名/手机号码：',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'name': 'username',
#             'id': 'id_username',
#         }),
#         required=True,
#         error_messages={'required':'不能为空','invalid':'格式错误'}
#     )
#     name = forms.CharField(
#         label=u'名字：',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'name': 'name',
#             'id': 'id_name',
#         }),
#     )

class RegisterForm(forms.Form):
    username=forms.CharField(
        max_length=16,
        label=u'用户名',
        widget=forms.TextInput(attrs={
            'class':'form-register',
            'name':'username',
            'id':'id_username',
            'placeholder':'username',
        }),
        required=True,
        error_messages={'required': '不能为空', 'invalid': '格式错误'}
    )
    CHOICES=[
        (u'男',u'男'),
        (u'女',u'女'),
    ]
    sex=forms.ChoiceField(
        label=u'',
        choices=CHOICES,
        widget=forms.RadioSelect(),
        initial=u'男',
    )
    password=forms.CharField(
        label=u'密码',
        widget=forms.PasswordInput(attrs={
            'class':'form-register',
            'id':'id_password',
        }),
    )
    re_password=forms.CharField(
        label=u'重复密码',
        widget=forms.PasswordInput(attrs={
            'class':'form-register',
            'name':'re_password',
        })
    )
    email=forms.CharField(
        label=u'邮箱',
        widget=forms.TextInput(attrs={
            'class': 'form-register',
            'name': 'email',
            'id': 'id_email',
        }),
        required=False,
    )

class LoginForm(forms.Form):
    username=forms.CharField(
        label=u'用户名',
        widget=forms.TextInput(attrs={
            'class':'form-login',
            'name':'username',
            'id':'id_username',
        })
    )
    # password=forms.CharField()