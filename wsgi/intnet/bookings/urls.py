# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from bookings import views

urlpatterns = patterns(
    '',
    url(r'^(?P<booking_id>\d+)/$', views.booking, name='booking'),
    url(r'^change_booking/(?P<booking_id>\d+)/(?P<change_id>\d+)/$', views.change_booking, name='change_booking'),
    url(r'^$', views.bookings, name='bookings'),
    url(r'^create/(?P<activity_id>\d+)/$', views.create_booking, name='create_booking'),
    url(r'^cancel/(?P<booking_id>\d+)/$', views.cancel_booking, name='cancel_booking'),
)
