from django.db.models.deletion import DO_NOTHING, PROTECT
from DTS.stock_models import Medicine
from django.db import models
from .stock_models import Medicine
import random

class Transaction(models.Model):
    def generate_num():
        
        serials=[]
        new=list(Transaction.objects.values_list('reference_number'))
        for n in new:
            for l in n:
                serials.append(l)
        not_unique = True
        while not_unique:
            x = f'SN{random.randint(10000000,99999999)}'
            if x not in serials:
                not_unique=False
        return x
    reference_number=models.CharField(max_length=10,blank=True,editable=False,unique=True,default=generate_num)
    transaction_type=models.CharField(max_length=30)
    medicine=models.ForeignKey(Medicine,on_delete=DO_NOTHING)
    description=models.TextField()
    quantity_measure=models.CharField(max_length=2)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.reference_number}'

# class Order(models.Model):
#     reference_number=models.IntegerField()
#     supplier=models.ForeignKey(Supplier, models.PROTECT)
#     total_quantity=models.IntegerField()
#     order_type=models.ForeignKey(OrderType,null=True,on_delete=models.SET_NULL)
#     order_price=models.FloatField()
#     order_date=models.DateTimeField()
#     order_status=models.CharField(max_length=3)
#     def __str__(self):
#         return f'{self.id}'

# class OrderedItem(models.Model):
#     medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE)
#     quantity=models.IntegerField()
#     customer_order=models.ForeignKey(Order, on_delete=models.CASCADE)
#     description=models.TextField()
#     def __str__(self):
#         return f'{self.id}'


# class Invoice(models.Model):
#     order=models.ForeignKey(Order,on_delete=models.CASCADE)
#     date_on_invoice=models.DateTimeField(auto_now_add=True)
#     total_price=models.FloatField()
#     status=models.CharField(max_length=30)
#     description=models.TextField()
#     def __str__(self):
#         return f'{self.id}'

# class Transaction(models.Model):
#     reference_number=models.IntegerField(unique=True)
#     date_issued=models.DateTimeField(auto_now_add=True)
#     description=models.TextField()
#     def __str__(self):
#         return f"{self.reference_number}"

# class AppointmentFee(models.Model):
#     amount=models.IntegerField()
#     patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
#     is_paid=models.BooleanField(default=False)
#     transaction=models.ForeignKey(Transaction,on_delete=models.PROTECT)


