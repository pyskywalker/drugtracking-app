from django.db import models
from django.db.models.deletion import DO_NOTHING
from .user_models import UserProfile as User
import random

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
    

class MedicineDetails(models.Model):
    name=models.CharField(max_length=30)
    manufacturer=models.CharField(max_length=30)
    description=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.manufacturer} {self.name}'
    

class MedicineType(models.Model):
    type_name=models.CharField(max_length=30)
    description=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.type_name}'

class Approval(models.Model):
    approver=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    status=models.BooleanField(default=False)
    date_approved=models.DateField(null=True,blank=True)
    description=models.TextField(blank=True,null=True)
class Batch(models.Model):
    medicine_detail=models.ForeignKey(MedicineDetails,on_delete=DO_NOTHING)
    batch_number=models.IntegerField()
    approval=models.ForeignKey(Approval,on_delete=models.PROTECT)
    unit_of_measure = models.IntegerField(default=100)
    concentration=models.CharField(max_length=15)
    description=models.TextField(blank=True,null=True)
    production_date=models.DateField()
    expiry_date=models.DateField()
    medicine_type=models.ForeignKey(MedicineType, on_delete=models.SET_NULL,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.batch_number}'
class Medicine(models.Model):
    def generate_num():
        serials=[]
        new=list(Medicine.objects.values_list('serial_number'))
        for n in new:
            for l in n:
                serials.append(l)
        not_unique = True
        while not_unique:
            x = f'SN{random.randint(10000000,99999999)}'
            if x not in serials:
                not_unique=False
        return x
    serial_number=models.CharField(max_length=10,blank=True,editable=False,unique=True,default=generate_num)
    
    quantity=models.IntegerField()
    used=models.IntegerField(blank=True,default=0)
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    stock_status=models.CharField(max_length=30,blank=True,null=True)
    batch=models.ForeignKey(Batch, on_delete=models.CASCADE)
    on_route=models.BooleanField(blank=True,default=False)
    def __str__(self):
        return f'{self.serial_number}'


   

# class Supplier(models.Model):
#     name=models.CharField(max_length=30)
#     address=models.CharField(max_length=50)
#     contacts=models.CharField(max_length=15)
#     def __str__(self):
#         return f'{self.name}'







    
