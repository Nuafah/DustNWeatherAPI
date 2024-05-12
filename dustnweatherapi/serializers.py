from rest_framework import serializers
from .models import BangkokDust, BangkokWeather, BangkokDustNWeather


class DustSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = BangkokDust


class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = BangkokWeather

class DustNWeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = BangkokDustNWeather