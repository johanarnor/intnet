# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^$', views.login_view, name='login'),
    url(r'^auth/$', views.authenticate_view, name='authenticate'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^sign_up/$', views.sign_up_view, name='sign_up'),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^save_user/$', views.save_user_view, name='save_user'),
    )