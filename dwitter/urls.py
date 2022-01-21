from django.urls import path,include

# from .views import dashboard
from .views.profileList import profile_list
from .views.dashboard import dashboard
from .views.profile import profile

app_name = "dwitter"

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('profile_list/',profile_list,name='profile_list'),
    path('profile/<int:pk>',profile,name='profile')

]
