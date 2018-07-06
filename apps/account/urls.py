#!/usr/bin/python3
from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url('signin/', views.Signin.as_view(), name='signin'),
    url('logout/', views.logout_view, name='logout'),
    url('user/', views.UserView.as_view(), name='user'),
    url('user_edit/(?P<user_id>.*)/', views.user_edit, name='user_edit'),
    url('upload/', views.save_img, name='upload'),
]