from django.db import models
from django.contrib.auth.models import User
from .hub_models import *
# Create your models here.

class UserType(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.id}:{self.name}'

class Profile(models.Model):
    actual_user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='system_users')
    title=models.CharField(max_length=30)
    location=models.ForeignKey(Location,on_delete=models.DO_NOTHING,null=True)
    user_type=models.ForeignKey(UserType,on_delete=models.SET_NULL,null=True)
    organization=models.CharField(max_length=50)
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.actual_user.username},{self.title},{self.user_type.name}"
