from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=32)
    kilometer = models.CharField(max_length=8, null=True)
    model = models.CharField(max_length=4)
    price = models.CharField(max_length=16)
