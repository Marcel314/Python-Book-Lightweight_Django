from django.conf.urls import patterns, include, url
from HolderApp import views

urlpatterns = patterns('',
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', views.placeholder,name='placeholder'),
    url(r'^$',views.index, name='homepage'),
)
