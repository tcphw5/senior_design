from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.landing, name='landing'),
    url(r'^Statistics/$', views.statistics, name='statistics'),
    url(r'^Rules/$', views.rules, name='rules'),
    url(r'^index/$', views.index, name='index'),
    url(r'^JoinGame/$', views.joingame, name='joingame'),
)
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.STATIC_ROOT}),
)
