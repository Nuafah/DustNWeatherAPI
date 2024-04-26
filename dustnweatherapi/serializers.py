from rest_framework import serializers
from .models import BangkokDust, BangkokWeather


class DustSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = BangkokDust


class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = BangkokWeather
