from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',

    url(r'^$', views.index),
    url(r'Statistics/$', views.statistics),
    url(r'Rules/$', views.rules)
)