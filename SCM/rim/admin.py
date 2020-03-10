from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Project)
admin.site.register(models.ReleaseInfo)
admin.site.register(models.Group)