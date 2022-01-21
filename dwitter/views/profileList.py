import imp
from django.shortcuts import render
from ..models.profileModel import Profile
# Create your views here.

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request,"dwitter/profile_list.html",{"profiles":profiles})