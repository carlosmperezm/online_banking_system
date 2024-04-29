from django.db import models
from datetime import date

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_date = models.DateField(default=date.today)
    balance = models.FloatField(default=2000)

    def __str__(self):
        return self.name

