from django.contrib import admin
from rbac import models


# Register your models here.

class PermissionAdmin(admin.ModelAdmin):
    list_display = ['url', 'title']
    list_editable = ['title']


admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.Role)
admin.site.register(models.User)
