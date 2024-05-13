from rest_framework import serializers
from .models import BangkokDust, BangkokWeather, BangkokDustNWeather


class DustSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BangkokDust


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BangkokWeather

class DustNWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BangkokDustNWeather