from django.conf.urls import url
from django.urls import path
from django.urls import re_path
from weiboAnalytics import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

from django.views.static import serve

urlpatterns = [
    url(r'weiboList/', views.weiboAnalytics, name='weiboAnalytics'),
    url(r'weiboPic/', views.weiboPic, name='weiboPic'),
    url(r'weiboKmeans/', views.weiboKmeans, name='weiboKmeans')
    #url(r'^medias/(?P<path>.*)$', serve, {'document_root': 'static/images'}),
    #path('weiboAnalytics/', views.weiboAnalytics, name='weiboAnalytics'),
]
urlpatterns += staticfiles_urlpatterns()