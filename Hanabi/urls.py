from django.conf.urls import patterns, url
from django.conf import settings
from . import views

app_name = 'Hanabi'
urlpatterns = patterns(
    '',
    url(r'^$', views.landing, name='landing'),
    url(r'^Statistics/$', views.statistics, name='statistics'),
    url(r'^Rules/$', views.rules, name='rules'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index/(?P<playernames>.+)/$', views.index, name='index'),
    url(r'^JoinGame/$', views.joingame, name='joingame'),
    url(r'^hello/$', views.hello, name='hello'),
)
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.STATIC_ROOT}),
)
