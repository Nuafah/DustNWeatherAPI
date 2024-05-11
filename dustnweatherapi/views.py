from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import DustSerializer, WeatherSerializer, DustNWeatherSerializer
from .models import BangkokWeather, BangkokDust, BangkokDustNWeather

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = BangkokWeather.objects.all()
    serializer_class = WeatherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

class DustViewSet(viewsets.ModelViewSet):
    queryset = BangkokDust.objects.all()
    serializer_class = DustSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

class DustNWeatherViewSet(viewsets.ModelViewSet):
    queryset = BangkokDustNWeather.objects.all()
    serializer_class = DustNWeatherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"
