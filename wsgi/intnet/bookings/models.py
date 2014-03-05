from django.db import models
from users.models import DirrUser
from activities.models import Activity, FeatureOption


class Booking(models.Model):

    def __unicode__(self):
        return unicode(self.activity)

    user = models.ForeignKey(DirrUser)
    activity = models.ForeignKey(Activity)
    amount = models.IntegerField(max_length=31)
    activity_date = models.DateTimeField()
    booking_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    paid = models.DateTimeField(null=True)


class BookingOption(models.Model):

    def __unicode__(self):
        return unicode(self.feature_option)

    booking = models.ForeignKey('Booking')
    feature_option = models.ForeignKey(FeatureOption)


class People(models.Model):

    def __unicode__(self):
        return unicode(self.label)

    label = models.CharField(max_length=255)
    booking = models.ForeignKey('Booking')
    adult = models.IntegerField(null=True)
    youth = models.IntegerField(null=True)
    child = models.IntegerField(null=True)
    student = models.IntegerField(null=True)
    senior = models.IntegerField(null=True)
