from rest_framework import serializers
from .stock_models import Medicine,Batch
from .user_models import Profile

# class MedicineBrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=MedicineBrand
# #         fields=['id','brand_name']
# class BatchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Batch
#         fields=['id','batch_number']
# # class ZoneSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model=MSDZone
# #         fields=['id','zone_name','zone-location']
# class MedicineSerializer(serializers.ModelSerializer):
#     batch=BatchSerializer()
#     class Meta:
#         model=Medicine
#         fields='__all__'
# class SupplierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Supplier
#         fields='__all__'