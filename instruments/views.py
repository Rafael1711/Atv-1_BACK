from rest_framework import generics
from .models import Instrument
from .serializers import InstrumentSerializer

class InstrumentListCreate(generics.ListCreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

class InstrumentRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer