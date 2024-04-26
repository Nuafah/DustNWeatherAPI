from rest_framework import viewsets
from .serializers import DustSerializer, WeatherSerializer
from .models import BangkokWeather, BangkokDust

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = BangkokWeather.objects.all()
    serializer_class = WeatherSerializer

class DustViewSet(viewsets.ModelViewSet):
    queryset = BangkokDust.objects.all()
    serializer_class = DustSerializer