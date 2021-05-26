# from .user_models import Profile
# from rest_framework import serializers
# from .user_models import *
# from knox.models import AuthToken

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id','first_name','last_name','username','password')
#         extra_kwargs = {'password': {'write_only': True}}
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['password'])
#         return user
# class UserTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Designation
#         fields="__all__"
# class UserSerializer(serializers.ModelSerializer):
#     usertype=Designation()
#     class Meta:
#         model=Profile
#         fields="__all__"
# class RestrictedUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Profile
#         fields=['id','first_name','last_name','room','usertype','phone']