"""QMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from apps.account.views import gettemplates
from apps.errors import views as error_views

urlpatterns = [
    url(r'', include('apps.report.urls', namespace='report')),
    # url(r'^question/',include('apps.question_track.urls',namespace='question')),
    url(r'^account/', include('apps.account.urls', namespace='account')),
    url(r'^admin/', admin.site.urls),
    url(r'^templates/(?P<templates>.*)/', gettemplates, name='templates'),
    url(r'^view_403/$', error_views.view_403, name='view_403'),
    url(r'^view_404/$', error_views.view_404, name='view_404'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


