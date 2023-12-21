from django.db import models

# Create your models here.


class StudentRecord(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=80)

class AdminInformation(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
