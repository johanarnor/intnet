from django.db import models


class Price(models.Model):

    def __unicode__(self):
        return unicode(self.label)

    label = models.CharField(max_length=255)
    adult = models.IntegerField()
    youth = models.IntegerField()
    child = models.IntegerField()
    student = models.IntegerField()
    senior = models.IntegerField()
    REQUIRED_FIELDS = ['adult']


class Activity(models.Model):

    def __unicode__(self):
        return unicode(self.label)

    label = models.CharField(max_length=255)
    description = models.TextField()
    price = models.ForeignKey('Price')
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now_add=True)
    purchases = models.IntegerField(default=0)


class CarouselImage(models.Model):

    def __unicode__(self):
        return unicode(self.title)

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='pics/carousel')
    activity = models.ForeignKey('Activity')


class Feature(models.Model):

    def __unicode__(self):
        return unicode(self.feature)

    feature = models.CharField(max_length=255)
    activity = models.ForeignKey('Activity')
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now_add=True)


class FeatureOption(models.Model):

    def __unicode__(self):
        return unicode(self.option)

    option = models.CharField(max_length=255)
    feature = models.ForeignKey('Feature')
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now_add=True)
