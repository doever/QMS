#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(
        max_length=16,
        label=u'用户名',
        widget=forms.TextInput(attrs={
            'class':'form-register',
            'name':'username',
            'id':'id_username',
            'placeholder':'username',
        })
    )
    CHIOCES=[
        (u'男',u'男'),
        (u'女',u'女'),
    ]
    sex=forms.ChoiceField(
        label=u'',
        chioces=CHIOCES,
        widget=forms.RadioSelect(),
        initial=u'男',
    )
    password=forms.CharField(
        lable=u'密码',
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
        widget=forms.EmailField(attrs={
            'class':'form-register',
            'name':'email',
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
    password=forms.CharField()