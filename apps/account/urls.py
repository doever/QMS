#!/usr/bin/python3
from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url('signin/',views.Signin.as_view(),name='signin'),
    url('add/',views.add_user,name='add'),
    url('user/',views.UserView.as_view(),name='user'),
]