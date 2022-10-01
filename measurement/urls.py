from django.urls import path

from measurement.views import GetCreateSensor, UpdateSensor, CreateMeasurement

urlpatterns = [
    path('sensors/', GetCreateSensor.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
]