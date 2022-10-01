from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import SensorDetailSerializer, MeasurementSerializer
from .models import Sensor, Measurement


class GetCreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateMeasurement(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
