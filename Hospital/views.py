from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response
from .models import UserProfile, HospitalRoom
from .serializers import UserProfileSerializer, UserSerializer,HospitalRoomsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox import views as knox_views
from django.http import HttpResponse
from django.contrib.auth import login
from knox.models import AuthToken
from rest_framework import request
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
class UsersAPI(generics.ListCreateAPIView):
    queryset=User.objects.filter(is_staff=False)
    serializer_class=UserSerializer

class RoomAPI(generics.ListCreateAPIView):
    queryset=HospitalRoom.objects.all()
    serializer_class=HospitalRoomsSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserSerializer
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class LoginAPI(KnoxLoginView):
    permission_classes = [AllowAny,]
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class UserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileView(generics.ListAPIView):
    permission_classes=[IsAuthenticated,]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class LoggedUserProfile(generics.RetrieveAPIView):
    queryset = UserProfile.objects  
    serializer_class = UserProfileSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, actual_user=self.request.user)
        return obj
    # def get_queryset(self):
    #     return self.queryset.filter(actual_user=self.request.user)