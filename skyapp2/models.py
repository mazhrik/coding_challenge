from django.db import models


# Create your models here.

class car(models.Model):
    name = models.TextField(default=" ")
    number_plate = models.TextField(default=" ")
    color = models.TextField(default=" ")


class shopping_cart(models.Model):
    shopping_number = models.IntegerField()
