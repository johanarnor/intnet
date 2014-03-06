import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from bookings.models import Booking
from django.contrib.auth.decorators import login_required
from bookings.models import Booking, People, BookingOption
from activities.models import Activity, FeatureOption


@login_required
def booking(request, booking_id):
    current_booking = Booking.objects.get(pk=booking_id)
    people = current_booking.people_set.all()
    p = people[0]
    total = p.senior + p.adult + p.youth + p.child + p.student
    return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'total': total})


@login_required
def bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/bookings.html', {'bookings': bookings})    return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'total': total})


def create_booking(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    user = request.user

    adults = int(request.POST['adults'])
    youths = int(request.POST['youths'])
    children = int(request.POST['children'])
    students = int(request.POST['students'])
    seniors = int(request.POST['seniors'])

    amount = adults + youths + children + students + seniors
    date_time = datetime.datetime(2014, 04, 23, 10, 00)  # TODO
    booking = Booking.objects.create(user=user, activity=activity, amount=amount, activity_date=date_time)

    peoples = People.objects.create(label=activity.label, booking=booking, adult=adults, youth=youths, child=children, student=students, senior=seniors)

    features = activity.feature_set.all()
    i = 1
    for feature in features:
        option = FeatureOption.objects.get(option=request.POST['feature' + str(i)])
        BookingOption.objects.create(booking=booking, feature_option=option)
        i = i + 1

    return HttpResponseRedirect(reverse('bookings:booking', args=(booking.pk,)))