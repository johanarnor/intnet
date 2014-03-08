import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from activities.forms import ActivityForm
from bookings.forms import PeopleForm, FeatureForm, DateForm
from django.contrib.auth.decorators import login_required
from bookings.models import Booking, People, BookingOption
from activities.models import Activity, FeatureOption


@login_required
def booking(request, booking_id):
    if Booking.objects.get(pk=booking_id).user != request.user:
        return HttpResponseRedirect(reverse('main:main'))

    if request.method == 'POST' and 'edit_people' in request.POST:
        current_booking = Booking.objects.get(pk=booking_id)
        form = PeopleForm(request.POST, booking=current_booking)
        if form.is_valid():
            form.save()
            people = current_booking.people_set.all()
            p = people[0]
            price = current_booking.activity.price
            current_booking.amount = p.adult*price.adult + p.youth*price.youth + p.child*price.child + p.student*price.student + p.senior*price.senior
            current_booking.save()
    elif request.method == 'POST' and 'edit_features' in request.POST:
        current_booking = Booking.objects.get(pk=booking_id)
        features = current_booking.activity.feature_set.all()
        old_options = BookingOption.objects.filter(booking=current_booking)
        old_options.delete()
        i = 1
        for feature in features:
            option = FeatureOption.objects.get(option=request.POST['feature' + str(i)])
            BookingOption.objects.create(booking=current_booking, feature_option=option)
            i += 1
    elif request.method == 'POST' and 'edit_date' in request.POST:
        current_booking = Booking.objects.get(pk=booking_id)
        print 'edit-date'
        dateStrings = request.POST['date'].split("/")
        month = dateStrings[0]
        day = dateStrings[1]
        year = dateStrings[2]
        date = datetime.date(int(year), int(month), int(day))

        current_booking.activity_date = date
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
    print change_id
    if change_id == '1':
        print 'feature'
        features = current_booking.activity.feature_set.all()
        form = FeatureForm(booking=current_booking, features=features)
        return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'feature_form': form, 'total': total})
    elif change_id == '2':
        print 'people'
        form = PeopleForm(instance=p, booking=current_booking)
        return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'people_form': form, 'total': total})
    elif change_id == '3':
        print 'date'
        form = DateForm(booking=current_booking)
        return render(request, 'bookings/booking.html', {'current_booking': current_booking, 'p': p, 'date_form': form, 'total': total})


@login_required
def bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    description_images = []
    for booking in bookings:
        description_images.append(booking.activity.descriptionimage_set.all()[0].image.url)

    bookings_images = zip(bookings, description_images)

    return render(request, 'bookings/bookings.html', {'bookings_images': bookings_images})

@login_required
def create_booking(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    features = activity.feature_set.all()

    if not ActivityForm(request.POST, features=features, activity=activity).is_valid():
        print "fel"
        return HttpResponseRedirect(reverse('activities:view_activity', args=(activity_id,)))

    user = request.user

    adults = int(request.POST['adults'])
    youths = int(request.POST['youths'])
    children = int(request.POST['children'])
    students = int(request.POST['students'])
    seniors = int(request.POST['seniors'])

    amount = adults + youths + children + students + seniors

    dateStrings = request.POST['date'].split("/")
    month = dateStrings[0]
    day = dateStrings[1]
    year = dateStrings[2]

    date_time = datetime.date(int(year), int(month), int(day))
    booking = Booking.objects.create(user=user, activity=activity, amount=amount, activity_date=date_time)
    activity.purchases += 1
    activity.save()

    peoples = People.objects.create(label=activity.label, booking=booking, adult=adults, youth=youths, child=children, student=students, senior=seniors)

    i = 1
    for feature in features:
        option = feature.featureoption_set.get(option=request.POST['feature' + str(i)])
        BookingOption.objects.create(booking=booking, feature_option=option)
        i = i + 1

    return HttpResponseRedirect(reverse('bookings:booking', args=(booking.pk,)))


def cancel_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    booking.people_set.all().delete()
    booking.delete()
    return HttpResponseRedirect(reverse('bookings:bookings'))
