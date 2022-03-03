from django.db import models

# Create your models here.

from django.db import models

from django.utils import timezone
import datetime


# Create your models here.
class vechile_m(models.Model):
    mileage = models.TextField(default='')
    number_plate_number = models.TextField(default='')
    manufacturer = models.TextField(default='')
    status = models.TextField(default='')


class date_vehicle(models.Model):
    number_plate_number = models.TextField(default='')
    mileage = models.TextField(default='')
    date = models.DateTimeField(editable=True)
