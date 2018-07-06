#!/usr/bin/python3
# -*- coding:utf-8 -*-
from django.shortcuts import render
__author__ = 'doever'
__date__ = '2018/7/7 1:08'


def view_403(request):
    return render(request, "403.html", status=403)


def view_404(request):
    return render(request,"404.html",status=404)



