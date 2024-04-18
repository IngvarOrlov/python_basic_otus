from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from myauth.models import MyUser

class MyUserAdmin(UserAdmin):
    pass

admin.site.register(MyUser, MyUserAdmin)