from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .serializers import DustSerializer, WeatherSerializer, DustNWeatherSerializer
from .models import BangkokWeather, BangkokDust, BangkokDustNWeather
from django.shortcuts import render, redirect
from django_filters import rest_framework as filter


class WeatherFilter(filter.FilterSet):
    condition_text = filter.CharFilter(field_name="condition_text", lookup_expr="iexact")
    temp_c_lte = filter.NumberFilter(field_name="temp_c", lookup_expr="lte")
    temp_c_gte = filter.NumberFilter(field_name="temp_c", lookup_expr="gte")
    wind_lte = filter.NumberFilter(field_name="wind_kph", lookup_expr="lte")
    wind_gte = filter.NumberFilter(field_name="wind_kph", lookup_expr="gte")
    humidity_lte = filter.NumberFilter(field_name="humidity", lookup_expr="lte")
    humidity_gte = filter.NumberFilter(field_name="humidity", lookup_expr="gte")
    cloud_lte = filter.NumberFilter(field_name="cloud", lookup_expr="lte")
    cloud_gte = filter.NumberFilter(field_name="cloud", lookup_expr="gte")


class DustFilter(filter.FilterSet):
    location = filter.CharFilter(field_name="location", lookup_expr="iexact")
    pm1_lte = filter.NumberFilter(field_name="pm1", lookup_expr="lte")
    pm1_gte = filter.NumberFilter(field_name="pm1", lookup_expr="gte")
    pm2_5_lte = filter.NumberFilter(field_name="pm2_5", lookup_expr="lte")
    pm2_5_gte = filter.NumberFilter(field_name="pm2_5", lookup_expr="gte")
    pm10_lte = filter.NumberFilter(field_name="pm10", lookup_expr="lte")
    pm10_gte = filter.NumberFilter(field_name="pm10", lookup_expr="gte")


class DustNWeatherFilter(filter.FilterSet):
    location = filter.CharFilter(field_name="location", lookup_expr="iexact")
    pm1_lte = filter.NumberFilter(field_name="pm1", lookup_expr="lte")
    pm1_gte = filter.NumberFilter(field_name="pm1", lookup_expr="gte")
    pm2_5_lte = filter.NumberFilter(field_name="pm2_5", lookup_expr="lte")
    pm2_5_gte = filter.NumberFilter(field_name="pm2_5", lookup_expr="gte")
    pm10_lte = filter.NumberFilter(field_name="pm10", lookup_expr="lte")
    pm10_gte = filter.NumberFilter(field_name="pm10", lookup_expr="gte")
    condition_text = filter.CharFilter(field_name="condition_text", lookup_expr="iexact")
    temp_c_lte = filter.NumberFilter(field_name="temp_c", lookup_expr="lte")
    temp_c_gte = filter.NumberFilter(field_name="temp_c", lookup_expr="gte")
    wind_lte = filter.NumberFilter(field_name="wind_kph", lookup_expr="lte")
    wind_gte = filter.NumberFilter(field_name="wind_kph", lookup_expr="gte")
    humidity_lte = filter.NumberFilter(field_name="humidity", lookup_expr="lte")
    humidity_gte = filter.NumberFilter(field_name="humidity", lookup_expr="gte")
    cloud_lte = filter.NumberFilter(field_name="cloud", lookup_expr="lte")
    cloud_gte = filter.NumberFilter(field_name="cloud", lookup_expr="gte")

class WeatherViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = BangkokWeather.objects.all()
    serializer_class = WeatherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    #filterset_fields = "__all__"
    filterset_class = WeatherFilter
    ordering_fields = ["id", "ts", "temp_c", "wind_kph", "humidity", "cloud"]


class DustViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = BangkokDust.objects.all()
    serializer_class = DustSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    #filterset_fields = "__all__"
    filterset_class = DustFilter
    ordering_fields = "__all__"
    
    
class DustNWeatherViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = BangkokDustNWeather.objects.all()
    serializer_class = DustNWeatherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    #filterset_fields = "__all__"
    filterset_class = DustNWeatherFilter
    ordering_fields = ["id", "ts", "temp_c", "wind_kph", "humidity", "cloud", "location", "pm1", "pm2_5", "pm10"]



    
def index(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        if location is not None:
            return redirect('detail', location)
        return redirect('index')
    else:
        dust_data = BangkokDustNWeather.objects.filter(location='bangkhen').all()
        dust_ts = [dust.ts.strftime('%Y-%m-%d') for dust in dust_data]
        dust_pm1 = [dust.pm1 for dust in dust_data]
        dust_pm2_5 = [dust.pm2_5 for dust in dust_data]
        dust_pm10 = [dust.pm10 for dust in dust_data]

        weather_data = BangkokDustNWeather.objects.filter(location='bangkhen').all()

        weather_condition = [weather.condition_text for weather in
                             weather_data]
        condition_count = {i: weather_condition.count(i) for i in
                           weather_condition}

        condition_key = list(condition_count.keys())
        condition_value = list(condition_count.values())

        wind_speed_data = [weather.wind_kph for weather in weather_data]
        avg_wind_kph = round(sum(wind_speed_data) / len(wind_speed_data), 2)
        temp_c_data = [weather.temp_c for weather in weather_data]
        avg_temp_c = round(sum(temp_c_data) / len(temp_c_data), 2)
        humidity_data = [weather.humidity for weather in weather_data]
        avg_humidity = round(sum(humidity_data) / len(humidity_data), 2)
        cloud_data = [weather.humidity for weather in weather_data]
        avg_cloud = round(sum(cloud_data) / len(cloud_data), 2)

        return render(request, "index.html", {
            'labels': dust_ts,
            'data': dust_pm2_5,
            'data1': dust_pm1,
            'data10': dust_pm10,
            'condition_key': condition_key,
            'condition_value': condition_value,
            'avg_wind_kph': avg_wind_kph,
            'avg_temp_c': avg_temp_c,
            'avg_humidity': avg_humidity,
            'avg_cloud': avg_cloud,
            'location': 'bangkhen'
        })


def detail(request, location):
    dust_data = BangkokDustNWeather.objects.filter(location=location).all()
    dust_ts = [dust.ts.strftime('%Y-%m-%d') for dust in dust_data]
    dust_pm1 = [dust.pm1 for dust in dust_data]
    dust_pm2_5 = [dust.pm2_5 for dust in dust_data]
    dust_pm10 = [dust.pm10 for dust in dust_data]

    weather_data = BangkokDustNWeather.objects.filter(location=location).all()

    weather_condition = [weather.condition_text for weather in weather_data]
    condition_count = {i: weather_condition.count(i) for i in
                       weather_condition}

    condition_key = list(condition_count.keys())
    condition_value = list(condition_count.values())

    wind_speed_data = [weather.wind_kph for weather in weather_data]
    print(len(wind_speed_data))
    avg_wind_kph = round(sum(wind_speed_data) / len(wind_speed_data), 2)
    temp_c_data = [weather.temp_c for weather in weather_data]
    avg_temp_c = round(sum(temp_c_data) / len(temp_c_data), 2)
    humidity_data = [weather.humidity for weather in weather_data]
    avg_humidity = round(sum(humidity_data) / len(humidity_data), 2)
    cloud_data = [weather.humidity for weather in weather_data]
    avg_cloud = round(sum(cloud_data) / len(cloud_data), 2)

    return render(request, "detail.html", {
        'labels': dust_ts,
        'data': dust_pm2_5,
        'data1': dust_pm1,
        'data10': dust_pm10,
        'condition_key': condition_key,
        'condition_value': condition_value,
        'avg_wind_kph': avg_wind_kph,
        'avg_temp_c': avg_temp_c,
        'avg_humidity': avg_humidity,
        'avg_cloud': avg_cloud,
        'location': location
    })
