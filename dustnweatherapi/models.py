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
