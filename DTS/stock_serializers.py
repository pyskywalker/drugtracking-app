from rest_framework import serializers
from .stock_models import Medicine,Batch
from .user_models import *

# class MedicineBrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=MedicineBrand
#         fields=['id','brand_name']
class BatchSerializer(serializers.ModelSerializer):
    medicine_type_name=serializers.CharField(source="medicine_type.type_name",read_only=True)
    class Meta:
        model=Batch
        fields=['id','batch_number']
# class ZoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=MSDZone
#         fields=['id','zone_name','zone-location']
class MedicineSerializer(serializers.ModelSerializer):
    batch_number=serializers.IntegerField(source="batch.batch_number",read_only=True)
    tmda_status=serializers.BooleanField(source="batch.tmda_status",read_only=True)
    expiry_date=serializers.CharField(source="batch.expiry_date",read_only=True)
    manufacturer=serializers.CharField(source="batch.manufactured_by",read_only=True)
    type=serializers.CharField(source="medicine_type.type_name",read_only=True)
    medicine_type=serializers.CharField(source="batch.medicine_type.type_name",read_only=True)
    class Meta:
        model=Medicine
        fields='__all__'
# class SupplierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Supplier
#         fields='__all__'