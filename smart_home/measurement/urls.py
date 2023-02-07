from django.urls import path

from measurement.views import SensorListView, SensorRetrieveUpdateView, MeasurementsCreateView, \
    SensorDetailView

urlpatterns = [
    path('sensorlist/', SensorListView.as_view()),
    path('sensorupdate/<pk>/', SensorRetrieveUpdateView.as_view()),
    path('measurements/', MeasurementsCreateView.as_view()),
    path('sensorlist/<pk>/', SensorDetailView.as_view())
]