from django.contrib import admin
from Models.models import UserModel, FaceProtection


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['sender', 'description']
    list_display_links = ['sender', 'description']


admin.site.register(UserModel, UserModelAdmin)

