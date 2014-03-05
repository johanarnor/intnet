from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class DirrUser(AbstractUser):

    phone_nr = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    p_code = models.ForeignKey('PCode', null=True)
    city = models.ForeignKey('City', null=True)


class PCode(models.Model):

    p_code = models.CharField(max_length=30)


class City(models.Model):

    city = models.CharField(max_length=30)