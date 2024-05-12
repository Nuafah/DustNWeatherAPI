import datetime

from django.db import models

class BangkokWeather(models.Model):
    """BangkokWeather model represents weather data retrieved from API"""
    name = models.CharField(max_length=100)
    ts = models.DateTimeField(default=datetime.datetime.now())
    temp_c = models.DecimalField(decimal_places=2, max_digits=10)
    condition_text = models.CharField(max_length=300)
    wind_kph = models.DecimalField(decimal_places=2, max_digits=10)
    humidity = models.DecimalField(decimal_places=2, max_digits=10)
    cloud = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = "bangkok_weather_daily"

    def __str__(self):
            return (f"Weather when {self.ts} in {self.name} will be {self.condition_text}. The temperature is {self.temp_c}"
                    f"with the humidity around {self.humidity}%")


class BangkokDust(models.Model):
    """BangkokDust model represents dust data retrieved from Dust Sensor"""
    ts = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(max_length=100)
    pm1 = models.DecimalField(decimal_places=2, max_digits=5)
    pm2_5 = models.DecimalField(decimal_places=2, max_digits=5)
    pm10 = models.DecimalField(decimal_places=2, max_digits=5)

    class Meta:
        db_table = "bangkok_dust_daily"

    def __str__(self):
        return (f"{self.location} has pm1 = {self.pm1} µ/cubic metre, pm2.5 = {self.pm2_5} "
                f"µ/cubic metre, pm10 = {self.pm10} µ/cubic metre")

class BangkokDustNWeather(models.Model):
    """BangkokDustNWeather model represents integrated Data from dust and weather data"""
    location = models.CharField(max_length=100)
    ts = models.DateTimeField(default=datetime.datetime.now())
    pm1 = models.DecimalField(decimal_places=2, max_digits=5)
    pm2_5 = models.DecimalField(decimal_places=2, max_digits=5)
    pm10 = models.DecimalField(decimal_places=2, max_digits=5)
    temp_c = models.DecimalField(decimal_places=2, max_digits=10)
    condition_text = models.CharField(max_length=300)
    wind_kph = models.DecimalField(decimal_places=2, max_digits=10)
    humidity = models.DecimalField(decimal_places=2, max_digits=10)
    cloud = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = "bangkok_dustnweather_daily"
