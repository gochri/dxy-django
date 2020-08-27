"""socialmediaanalytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from django.views.static import serve

urlpatterns = [
    url(r'^weiboAnalytics/', include('weiboAnalytics.urls')),
    #url(r'^weiboPic/', include('weiboAnalytics.urls')),
    url(r'^sentimentanalysis/', include('sentimentanalysis.urls')),
    url(r'^images/(?P<path>.*)$', serve, {'document_root': 'static/images'}),
    url(r'^css/(?P<path>.*)$', serve, {'document_root': 'static/css'}),
    url(r'^js/(?P<path>.*)$', serve, {'document_root': 'static/js'}),
    url(r'^json/(?P<path>.*)$', serve, {'document_root': 'static/json'}),
    #url(r'^static/(?P<path>.*)$', serve, {'document_root': 'static'}),
    #url(r'^admin/', admin.site.urls),
    #url(r'^$/', index,name='index'),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
