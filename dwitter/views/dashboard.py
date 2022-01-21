import imp
from django.shortcuts import render,redirect
from dwitter.forms import DweetForm

from dwitter.models.dweetModel import Dweet
from dwitter.models.profileModel import Profile
# Create your views here.

def dashboard(request,):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
    
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by('created_at')
    print('aa: ',followed_dweets)
    form = DweetForm()
    return render(request,"dwitter/dashboard.html",{"form":form,"dweets":followed_dweets})