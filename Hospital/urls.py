from django.urls import path
from django.contrib import admin
from .views import LoggedUserProfile, UserProfileView,UserAPI,LoginAPI


urlpatterns = [
    path('userprofile/',LoggedUserProfile.as_view(), name='singleuserprofile'),
    path('user/',UserProfileView.as_view(),name="userprofile"),
    path('login/',LoginAPI.as_view(),name="login"),
]
