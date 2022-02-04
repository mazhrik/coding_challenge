from django.db import models


# Create your models here.
class vechile_model(models.Model):
    """
    model of vvechile
    """
    # INACTIVE = 0
    # ACTIVE = 1
    # STATUS = (
    #     (INACTIVE, ('Inactive')),
    #     (ACTIVE, ('Active')),
    # )

    mileage = models.TextField(default='')
    manufacturer = models.TextField(default='')
    status = models.TextField(default='')
    # active = models.BooleanField(default=0, choices=STATUS)
