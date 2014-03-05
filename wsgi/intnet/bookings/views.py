from django.shortcuts import render
from bookings.models import Booking

def booking(request, booking_id):
    current_booking = Booking.objects.get(pk=booking_id);
    return render(request, 'bookings/booking.html', {'current_booking': current_booking})
