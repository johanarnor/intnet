from django.contrib import admin
from bookings.models import Booking, BookingOption, People


admin.site.register(Booking)
admin.site.register(BookingOption)
admin.site.register(People)
