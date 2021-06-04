from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer

from DTS.hub_models import *
from DTS.user_models import *
from DTS.stock_models import *
from DTS.transaction_models import *
from DTS.hub_serializers import *
from DTS.stock_serializers import *
from DTS.transaction_serializers import *
from DTS.user_serializers import *
# Create your views here.


#############################USER_VIEWS#############################
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
class UserProfileView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = RestrictedUserSerializer

class LoggedUserProfile(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects  
    serializer_class = UserProfileSerializer
    def get_object(self):
        obj = get_object_or_404(self.queryset, actual_user=self.request.user)
        return obj


#############################STOCK_VIEWS############################
class MedicineAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Medicine.objects.all()
    serializer_class=MedicineSerializer
class BatchAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Batch.objects.all()
    serializer_class=BatchSerializer
#############################HUB_VIEWS############################
class InstituteAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Institute.objects.all()
    serializer_class=InstituteSerializer
class LocationAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Local.objects.all()
    serializer_class=LocationSerializer

#############################TRANSACTION_VIEWS############################
class TransactionAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TransactionSerializer
    lookup_url_kwarg = 'id'
    queryset=Transaction.objects.all()
