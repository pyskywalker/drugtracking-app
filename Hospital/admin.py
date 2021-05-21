from django.contrib import admin
from .models import *
# Register your models here.
mymodels=[UserProfile,UserType,HospitalRoom]
for model in mymodels:
    admin.site.register(model)