# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from activities import views

urlpatterns = patterns('',
    url(r'^(?P<activity_id>\d+)/$', views.view_activity, name='view_activity'),
)
