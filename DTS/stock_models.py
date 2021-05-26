from django.db import models

# Create your models here.
from django.utils import timezone
from .user_models import UserProfile as User

# Create your models here.
# class MSDZone(models.Model):
#     zone_name=models.CharField(max_length=50)
#     zone_location=models.CharField(max_length=30)
#     description=models.TextField()
#     date_added=models.DateTimeField(auto_now_add=True)
#     date_modified=models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f'{self.zone_name}'
    

# class MedicineBrand(models.Model):
#     brand_name=models.CharField(max_length=50)
#     location=models.CharField(max_length=50)
#     description=models.TextField()
#     date_added=models.DateTimeField(auto_now_add=True)
#     date_modified=models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f'{self.brand_name}'
    

class Batch(models.Model):
    batch_number=models.IntegerField()
    TMDA_verified=models.BooleanField(default=True)
    description=models.TextField()
    expiry_date=models.CharField(max_length=20)
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.batch_number}'
   

class Medicine(models.Model):
    serial_number=models.CharField(max_length=20)
    unit_of_measure = models.CharField(max_length=2)
    quantity=models.IntegerField()
    used=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=30)
    batch=models.ForeignKey(Batch, on_delete=models.CASCADE)
    on_route=models.BooleanField()
    def __str__(self):
        return f'{self.serialnumber}'
   

# class Supplier(models.Model):
#     name=models.CharField(max_length=30)
#     address=models.CharField(max_length=50)
#     contacts=models.CharField(max_length=15)
#     def __str__(self):
#         return f'{self.name}'







    