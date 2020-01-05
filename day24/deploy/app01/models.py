from django.db import models

# Create your models here.

class Server(models.Model):

    hostname = models.CharField(verbose_name='主机名', max_length=32)