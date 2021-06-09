from django.urls import path
from .views import *


urlpatterns = [
    path('userprofile/',LoggedUserProfile.as_view(), name='singleuserprofile'),
    path('userslist/',UserProfileView.as_view(),name="userprofile"),
    path('stock/medicine',MedicineAPI.as_view(),name="medicine"),
    path('stock/medicine/<int:id>',MedicineDetailView.as_view(),name="medicine"),
    path('stock/batches',BatchAPI.as_view(),name="batch"),
    path('transactions/',TransactionAPI.as_view(),name="transactions"),
    path('transactions/details/',TransactionDetailView.as_view(),name="transaction_details"),
    path('hub/institute/',InstituteAPI.as_view(),name="institute"),
    path('hub/location',LocationAPI.as_view(),name="location"),
]