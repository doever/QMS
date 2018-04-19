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
