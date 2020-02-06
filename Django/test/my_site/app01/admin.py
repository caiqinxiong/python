from django.contrib import admin
from app01.models import *
# Register your models here.
class AccoutAdmin(admin.ModelAdmin):
    list_display = ['username','email']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','conten']


admin.site.register(Account,AccoutAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag)