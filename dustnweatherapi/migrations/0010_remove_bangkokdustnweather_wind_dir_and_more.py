# Generated by Django 4.2.4 on 2024-05-12 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dustnweatherapi', '0009_bangkokdustnweather_remove_bangkokdust_lat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bangkokdustnweather',
            name='wind_dir',
        ),
        migrations.RemoveField(
            model_name='bangkokweather',
            name='wind_dir',
        ),
        migrations.AlterField(
            model_name='bangkokdust',
            name='ts',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 21, 17, 26, 152355)),
        ),
        migrations.AlterField(
            model_name='bangkokdustnweather',
            name='ts',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 21, 17, 26, 153352)),
        ),
        migrations.AlterField(
            model_name='bangkokweather',
            name='ts',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 21, 17, 26, 152355)),
        ),
        migrations.AlterModelTable(
            name='bangkokdust',
            table='bangkok_dust_daily',
        ),
        migrations.AlterModelTable(
            name='bangkokdustnweather',
            table='bangkok_dustnweather_daily',
        ),
        migrations.AlterModelTable(
            name='bangkokweather',
            table='bangkok_weather_daily',
        ),
    ]
