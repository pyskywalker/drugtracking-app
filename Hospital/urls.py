from django.urls import path
from .views import *


urlpatterns = [
    path('userprofile/',LoggedUserProfile.as_view(), name='singleuserprofile'),
    path('userslist/',UserProfileView.as_view(),name="userprofile"),
    path('pharmacy/medicine',MedicineAPI.as_view(),name="medicine"),
    path('pharmacy/batches',BatchAPI.as_view(),name="batch"),
    path('pharmacy/suppliers',SupplierAPI.as_view(),name="suppliers"),
]
