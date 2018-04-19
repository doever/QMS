#!/usr/bin/python3
from django.conf.urls import url
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings

import question_track.views as views

urlpatterns = [
                  # url(r'^$', views.index, name='index'),
                  url(r'^login/', views.user_login, name='user_login'),
                  url(r'^home$', views.qms_main, name='qms_main'),
                  url(r'^resginter/$',views.resginter,name='resginter'),
                  url(r'^report/$',views.resginter,name='report'),
                  url(r'^project_detils/$',views.resginter,name='project_detils'),
                  # url(r'^logout/', views.user_logout, name='user_logout'),
                  # url(r'^register/', views.user_register, name='user_register'),
                  # url(r'^set_password/', views.set_password, name='set_password'),
                  # url(r'^static/(?P<path>.*)$', static_views.serve, name='static'),
                  # url(r'^search/', views.book_search, name='book_search'),
                  # url(r'^profile/', views.profile, name='profile'),
                  # url(r'^statistics/', views.statistics, name='statistics'),
                  # url(r'^about/', views.about, name='about'),
              ]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)