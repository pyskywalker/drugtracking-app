from rest_framework import serializers
from .hospital_models import PatientType,Patient,Appointment,Labtest,LabTestItem,Diagnoses
from .user_serializers import UserProfileSerializer,UserSerializer
# from Pharmacy.serializers import MedicineBrandSerializer
from rest_framework import serializers

class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientType
        fields=['id','name','description']
class PatientSerializer(serializers.ModelSerializer):
    # patient_type=PatientTypeSerializer()
    class Meta:
        model=Patient
        fields='__all__'
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'
class LabtestSerializer(serializers.ModelSerializer):
    # appointment=AppointmentSerializer()
    # technician=UserSerializer()
    class Meta:
        model=Labtest
        fields='__all__'
class LabTestItemSerializer(serializers.ModelSerializer):
    # test=LabtestSerializer()
    class Meta:
        model=LabTestItem
        fields='__all__'
class DiagnosesSerializer(serializers.ModelSerializer):
    # appointment=AppointmentSerializer()
    class Meta:
        model=Diagnoses
        fields='__all__'