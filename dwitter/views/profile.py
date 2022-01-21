from django.shortcuts import render
from ..models.profileModel import Profile
# Create your views here.

def profile(request,pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile 
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    
    return render(request,"dwitter/profile.html",{"profile":profile})