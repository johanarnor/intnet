from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class DirrUser(AbstractUser):

    phone_nr = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    p_code = models.IntegerField(max_length=5, null=True)
    city = models.ForeignKey('City', null=True)


class City(models.Model):

    def __unicode__(self):
        return unicode(self.city)

    city = models.CharField(max_length=30)