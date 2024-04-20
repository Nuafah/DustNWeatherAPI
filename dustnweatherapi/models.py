from django.db import models

class BangkokWeather(models.Model):
    """BangkokWeather model represents weather data retrieved from API"""
    name = models.CharField(max_length=100)
    lat = models.DecimalField(decimal_places=2, max_digits=5)
    lon = models.DecimalField(decimal_places=2, max_digits=5)
    ts = models.DateTimeField()
    last_updated = models.TimeField()
    temp_c = models.DecimalField(decimal_places=2, max_digits=4)
    feelslike_c = models.DecimalField(decimal_places=2, max_digits=4)
    condition_text = models.CharField(max_length=300)
    wind_kph = models.DecimalField(decimal_places=2, max_digits=4)
    wind_dir = models.CharField(max_length=3)
    humidity = models.DecimalField(decimal_places=2, max_digits=4)
    cloud = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
            return (f"Weather when {self.ts} in {self.name} will be {self.condition_text}. The temperature is {self.temp_c}"
                    f"that feels like {self.feelslike_c} with the humidity around {self.humidity}%")


class BangkokDust(models.Model):
    """BangkokDust model represents dust data retrieved from Dust Sensor"""
    ts = models.DateTimeField
    location = models.CharField(max_length=100)
    lat = models.DecimalField(decimal_places=2, max_digits=5)
    lon = models.DecimalField(decimal_places=2, max_digits=5)
    pm1 = models.DecimalField(decimal_places=2, max_digits=5)
    pm2_5 = models.DecimalField(decimal_places=2, max_digits=5)
    pm10 = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return (f"{self.location} has pm1 = {self.pm1} µ/cubic metre, pm2.5 = {self.pm2_5} "
                f"µ/cubic metre, pm10 = {self.pm10} µ/cubic metre")
