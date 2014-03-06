from django.shortcuts import render
from bookings.models import Booking


def booking(request, booking_id):
    current_booking = Booking.objects.get(pk=booking_id)
    people = current_booking.people_set.all()
    p = people[0]
    total = p.senior + p.adult + p.youth + p.child + p.student
    return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'total': total})