# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from bookings import views

urlpatterns = patterns(
    '',
    url(r'^(?P<booking_id>\d+)/$', views.booking, name='booking'),
    url(r'^$', views.bookings, name='bookings'),
    url(r'^create/(?P<activity_id>\d+)/$', views.create_booking, name='create_booking'),
)
