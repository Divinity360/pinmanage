from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime


# Create your models here.
class Pin(models.Model):
    NETWORK_CHOICES = (
        ('MTN', 'MTN'),
        ('GLO', 'GLO'),
        ('AIRTEL', 'AIRTEL'),
        ('9MOBILE', '9MOBILE'),
    )

    NETWORK_VALUES = (
        ('100', '100'),
        ('200', '200'),
        ('500', '500'),
        ('1000', '1000'),
        ('1500', '1500'),
        ('2000', '2000'),
    )

    network = models.CharField(max_length=10, choices=NETWORK_CHOICES)
    value = models.CharField(max_length=4, choices=NETWORK_VALUES)
    pin = models.CharField(max_length=16, validators=[RegexValidator(r'^[0-9]{16}$')])


class SoldPin(models.Model):
    SOLDPINS_CHOICES = (
        ('MTN', 'MTN'),
        ('GLO', 'GLO'),
        ('AIRTEL', 'AIRTEL'),
        ('9MOBILE', '9MOBILE'),
    )

    SOLDPINS_VALUES = (
        ('100', '100'),
        ('200', '200'),
        ('500', '500'),
        ('1000', '1000'),
        ('1500', '1500'),
        ('2000', '2000'),
    )

    networksold = models.CharField(max_length=10, choices=SOLDPINS_CHOICES)
    valuesold = models.CharField(max_length=4, choices=SOLDPINS_VALUES)
    pinsold = models.CharField(max_length=16, validators=[RegexValidator(r'^[0-9]{16}$')])
    datesold = models.DateTimeField(auto_now=True)
