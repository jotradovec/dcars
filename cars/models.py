from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)
    maximum_speed = models.IntegerField(null=True, blank=True)
    acquired_date = models.DateField(null=True)

    def __str__(self):
        return self.name
