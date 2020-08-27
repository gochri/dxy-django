from django.conf.urls import url
from sentimentanalysis import views
urlpatterns = [
    #url(r'^$', views.DXYAnalytics, name='DXYAnalytics'),
    url(r'DXYAnalytics/', views.DXYAnalytics, name='DXYAnalytics'),
    url(r'D3Analytics/', views.D3Analytics, name='D3Analytics')
]