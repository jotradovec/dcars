from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)
    maximum_speed = models.IntegerField(null=True)
    acquired_date = models.DateField(null=True)
