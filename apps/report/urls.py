from django.conf.urls import url
from apps.report import views

app_name = 'report'
urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'test/',views.test,name='test'),
]
