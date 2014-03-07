import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from bookings.forms import PeopleForm
from django.contrib.auth.decorators import login_required
from bookings.models import Booking, People, BookingOption
from activities.models import Activity, FeatureOption


@login_required
def booking(request, booking_id):
    if request.method == 'POST' and 'adult' in request.POST:
        current_booking = Booking.objects.get(pk=booking_id)
        form = PeopleForm(request.POST, booking=current_booking)
        form.save()
        people = current_booking.people_set.all()
        p = people[0]
        price = current_booking.activity.price
        current_booking.amount = p.adult*price.adult + p.youth*price.youth + p.child*price.child + p.student*price.student + p.senior*price.senior
        current_booking.save()
    current_booking = Booking.objects.get(pk=booking_id)
    people = current_booking.people_set.all()
    p = people[0]
    total = p.senior + p.adult + p.youth + p.child + p.student
    return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'total': total})


@login_required
def change_booking(request, booking_id, change_id):
    current_booking = Booking.objects.get(pk=booking_id)
    people = current_booking.people_set.all()
    p = people[0]
    total = p.senior + p.adult + p.youth + p.child + p.student
    if change_id == 1:
        form = PeopleForm(instance=p, booking=current_booking)
        return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'people_form': form, 'total': total})
    elif change_id == 2:
        form = PeopleForm(instance=p, booking=current_booking)
        return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'people_form': form, 'total': total})
    else:
        form = PeopleForm(instance=p, booking=current_booking)
        return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'people_form': form, 'total': total})


@login_required
def bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/bookings.html', {'bookings': bookings})

@login_required
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