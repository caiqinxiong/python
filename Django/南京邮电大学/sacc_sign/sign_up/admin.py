from django.contrib import admin

from sign_up.models import Team_info,Actor_info,EmailVerifyRecord
# Register your models here.

admin.site.register(Team_info)
admin.site.register(Actor_info)
admin.site.register(EmailVerifyRecord)
