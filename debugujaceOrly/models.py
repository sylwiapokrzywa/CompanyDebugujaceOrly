from django.db import models


# Create your models here.
class Company(models.Model):
    city = models.CharField(max_length=260)
