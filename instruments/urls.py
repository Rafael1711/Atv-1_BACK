from django.urls import path
from . views import InstrumentListCreate, InstrumentRetrieveDestroy

urlpatterns = [
    path('instruments/', InstrumentListCreate.as_view(), name='instrument-list'),
    path('instruments/<int:pk>/', InstrumentRetrieveDestroy.as_view(), name='instrument-detail'),
]