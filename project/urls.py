from django.urls import path,include
from django.contrib import admin
from Hospital.views import LoginAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/v1/hospital/',include('Hospital.urls')),
    path('apis/v1/login/',LoginAPI.as_view(),name="login")
]
