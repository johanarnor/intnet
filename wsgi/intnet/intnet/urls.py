from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/', include('users.urls', namespace='users')),
                       url(r'^', include('main.urls', namespace='main')),
                       url(r'^activities/', include('activities.urls', namespace='activities')),
                       url(r'^bookings/', include('bookings.urls', namespace='bookings')),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
