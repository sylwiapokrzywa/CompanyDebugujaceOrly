from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=260)
    address = models.CharField(max_length=200)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()

    def __str__(self):
        return self.name