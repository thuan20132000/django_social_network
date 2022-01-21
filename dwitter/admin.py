from cProfile import Profile
from django.contrib import admin
from django.contrib.auth import models

# Register your models here.
from django.contrib.auth.models import Group, User

from dwitter.models.profileModel import Profile
from dwitter.models.dweetModel import Dweet

class ProfileInline(admin.StackedInline):
    model = Profile
        

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Dweet)

# admin.site.register(Profile)