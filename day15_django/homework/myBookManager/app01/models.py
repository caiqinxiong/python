from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32)  # varchar(32)
    password = models.CharField(max_length=32)  # varchar(32)

class Publisher(models.Model):
    name = models.CharField(max_length=32)