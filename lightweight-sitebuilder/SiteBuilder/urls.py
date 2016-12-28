from django.conf.urls import patterns, include, url
from SiteBuilderApp import views as v
urlpatterns = patterns('',
    url(r'^(?P<slug>[\w./-]+)/$', v.page, name='page'),
    url(r'^$', v.page, name='homepage'),
)
