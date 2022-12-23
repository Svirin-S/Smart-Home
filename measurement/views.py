from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Measurement, Sensor
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorAPIList(ListCreateAPIView):
    queryset = Sensor.objects.all() 
    serializer_class = SensorSerializer  


class SensorAPIListFull(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorAPIUpdate(UpdateAPIView):
    queryset = Sensor.objects.all() 
    serializer_class = SensorSerializer  


class SensorAPIDelete(DestroyAPIView):
    queryset = Sensor.objects.all()  
    serializer_class = SensorDetailSerializer     


class MeasAPIList(ListCreateAPIView):
    queryset = Measurement.objects.all() 
    serializer_class = MeasurementSerializer 








