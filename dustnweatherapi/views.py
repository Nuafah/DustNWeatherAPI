from rest_framework import viewsets
from .serializers import DustSerializer, WeatherSerializer
from .models import BangkokWeather, BangkokDust,BangkokDustNWeather
from django.shortcuts import render, redirect


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = BangkokWeather.objects.all()
    serializer_class = WeatherSerializer


class DustViewSet(viewsets.ModelViewSet):
    queryset = BangkokDust.objects.all()
    serializer_class = DustSerializer


def index(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        if location is not None:
            return redirect('detail', location)
        return redirect('index')
    else:
        dust_data = BangkokDustNWeather.objects.all()
        dust_ts = [dust.ts.strftime('%Y-%m-%d') for dust in dust_data]
        dust_pm1 = [dust.pm1 for dust in dust_data]
        dust_pm2_5 = [dust.pm2_5 for dust in dust_data]
        dust_pm10 = [dust.pm10 for dust in dust_data]

        weather_data = BangkokDustNWeather.objects.all()

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
            'avg_cloud': avg_cloud
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
        'avg_cloud': avg_cloud
    })
