from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',

    url(r'^$', views.landing, name='landing'),
    url(r'Statistics/$', views.statistics, name='statistics'),
    url(r'Rules/$', views.rules, name='rules'),
    url(r'index/$', views.index, name='index')
)