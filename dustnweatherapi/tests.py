import time
from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIClient
from .models import BangkokWeather, BangkokDust, BangkokDustNWeather


class BaseTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create mock data with timestamps in the required format
        ts_format = "%Y-%m-%d %H:%M:%S"
        ts1 = datetime.strptime("2024-05-01 07:00:00", ts_format)
        ts2 = datetime.strptime("2024-05-02 07:00:00", ts_format)
        ts3 = datetime.strptime("2024-05-03 07:00:00", ts_format)

        # Convert datetime objects to strings in the required format
        ts1_str = ts1.strftime(ts_format)
        ts2_str = ts2.strftime(ts_format)
        ts3_str = ts3.strftime(ts_format)

        #create weather data
        self.weather1 = BangkokWeather.objects.create(id=1,
                                                     temp_c=30.12,
                                                     name='place1',
                                                     ts=ts1_str,
                                                     condition_text="Partly cloudy",
                                                     wind_kph=20.12,
                                                     humidity=35.12,
                                                     cloud=40.12)

        self.weather2 = BangkokWeather.objects.create(id=2,
                                                     temp_c=27.12,
                                                     name='place2',
                                                     ts=ts2_str,
                                                     condition_text="Clear",
                                                     wind_kph=25.12,
                                                     humidity=25.12,
                                                     cloud=20.12)

        self.weather3 = BangkokWeather.objects.create(id=3,
                                                     temp_c=40.12,
                                                     name='place3',
                                                     ts=ts3_str,
                                                     condition_text="Sunny",
                                                     wind_kph=30.12,
                                                     humidity=50.12,
                                                     cloud=50.12)

        #create dust data
        self.dust1 = BangkokDust.objects.create(id=1,
                                                location="loc1",
                                                ts=ts1_str,
                                                pm1=12.12,
                                                pm2_5=30.12,
                                                pm10=50.12,
                                                )
        self.dust2 = BangkokDust.objects.create(id=2,
                                                location="loc2",
                                                ts=ts2_str,
                                                pm1=15.12,
                                                pm2_5=35.12,
                                                pm10=57.12,
                                                )
        self.dust3 = BangkokDust.objects.create(id=3,
                                                location="loc3",
                                                ts=ts3_str,
                                                pm1=18.12,
                                                pm2_5=38.12,
                                                pm10=59.12,
                                                )

        #create dustnweather data
        self.dustnweather1 = BangkokDustNWeather.objects.create(id=1,
                                                location="loc1",
                                                ts=ts1_str,
                                                pm1=12.12,
                                                pm2_5=30.12,
                                                pm10=50.12,
                                                temp_c=30.12,
                                                condition_text="Partly cloudy",
                                                wind_kph=20.12,
                                                humidity=35.12,
                                                cloud=40.12)

        self.dustnweather2 = BangkokDustNWeather.objects.create(id=2,
                                                location="loc2",
                                                ts=ts2_str,
                                                pm1=15.12,
                                                pm2_5=35.12,
                                                pm10=57.12,
                                                temp_c=27.12,
                                                condition_text="Clear",
                                                wind_kph=25.12,
                                                humidity=25.12,
                                                cloud=20.12)
        self.dustnweather3 = BangkokDustNWeather.objects.create(id=3,
                                                location="loc3",
                                                ts=ts3_str,
                                                pm1=18.12,
                                                pm2_5=38.12,
                                                pm10=59.12,
                                                temp_c=40.12,
                                                condition_text="Sunny",
                                                wind_kph=30.12,
                                                humidity=50.12,
                                                cloud=50.12)
        self.expected_weather1 ={
            'id': self.weather1.id,
            'name': self.weather1.name,
            'ts': '2024-05-01T07:00:00+07:00',
            'temp_c': str(self.weather1.temp_c),
            'condition_text': self.weather1.condition_text,
            'wind_kph': str(self.weather1.wind_kph),
            'humidity': str(self.weather1.humidity),
            'cloud': str(self.weather1.cloud),

        }

        self.expected_weather2 = {
            'id': self.weather2.id,
            'name': self.weather2.name,
            'ts': '2024-05-02T07:00:00+07:00',
            'temp_c': str(self.weather2.temp_c),
            'condition_text': self.weather2.condition_text,
            'wind_kph': str(self.weather2.wind_kph),
            'humidity': str(self.weather2.humidity),
            'cloud': str(self.weather2.cloud),

        }
        self.expected_weather3 = {
            'id': self.weather3.id,
            'name': self.weather3.name,
            'ts': '2024-05-03T07:00:00+07:00',
            'temp_c': str(self.weather3.temp_c),
            'condition_text': self.weather3.condition_text,
            'wind_kph': str(self.weather3.wind_kph),
            'humidity': str(self.weather3.humidity),
            'cloud': str(self.weather3.cloud),

        }

        self.expected_dust1 = {
            'id': self.dust1.id,
            'location': self.dust1.location,
            'ts': '2024-05-01T07:00:00+07:00',
            'pm1': str(self.dust1.pm1),
            'pm2_5': str(self.dust1.pm2_5),
            'pm10': str(self.dust1.pm10),

        }

        self.expected_dust2 = {
            'id': self.dust2.id,
            'location': self.dust2.location,
            'ts': '2024-05-02T07:00:00+07:00',
            'pm1': str(self.dust2.pm1),
            'pm2_5': str(self.dust2.pm2_5),
            'pm10': str(self.dust2.pm10),

        }

        self.expected_dust3 = {
            'id': self.dust3.id,
            'location': self.dust3.location,
            'ts': '2024-05-03T07:00:00+07:00',
            'pm1': str(self.dust3.pm1),
            'pm2_5': str(self.dust3.pm2_5),
            'pm10': str(self.dust3.pm10),

        }

        self.expected_dustnweather1 = {
            'id': self.dustnweather1.id,
            'location': self.dustnweather1.location,
            'ts': '2024-05-01T07:00:00+07:00',
            'pm1': str(self.dustnweather1.pm1),
            'pm2_5': str(self.dustnweather1.pm2_5),
            'pm10': str(self.dustnweather1.pm10),
            'temp_c': str(self.dustnweather1.temp_c),
            'condition_text': self.dustnweather1.condition_text,
            'wind_kph': str(self.dustnweather1.wind_kph),
            'humidity': str(self.dustnweather1.humidity),
            'cloud': str(self.dustnweather1.cloud),

        }

        self.expected_dustnweather2 = {
            'id': self.dustnweather2.id,
            'location': self.dustnweather2.location,
            'ts': '2024-05-02T07:00:00+07:00',
            'pm1': str(self.dustnweather2.pm1),
            'pm2_5': str(self.dustnweather2.pm2_5),
            'pm10': str(self.dustnweather2.pm10),
            'temp_c': str(self.dustnweather2.temp_c),
            'condition_text': self.dustnweather2.condition_text,
            'wind_kph': str(self.dustnweather2.wind_kph),
            'humidity': str(self.dustnweather2.humidity),
            'cloud': str(self.dustnweather2.cloud),

        }

        self.expected_dustnweather3 = {
            'id': self.dustnweather3.id,
            'location': self.dustnweather3.location,
            'ts': '2024-05-03T07:00:00+07:00',
            'pm1': str(self.dustnweather3.pm1),
            'pm2_5': str(self.dustnweather3.pm2_5),
            'pm10': str(self.dustnweather3.pm10),
            'temp_c': str(self.dustnweather3.temp_c),
            'condition_text': self.dustnweather3.condition_text,
            'wind_kph': str(self.dustnweather3.wind_kph),
            'humidity': str(self.dustnweather3.humidity),
            'cloud': str(self.dustnweather3.cloud),

        }

class TestWeather(BaseTest):
    def test_get_all_weather(self):
        """
        Test if the user can retrieve all data from weather table

        Retrieve a data of all weather in json format
        """
        response = self.client.get("/api/weather/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather1,
                                           self.expected_weather2,
                                           self.expected_weather3])


    def test_get_weather_id(self):
        """
        Test if the user can retrieve a data from weather table by specifying the id.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_weather1)

        response = self.client.get("/api/weather/2/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_weather2)

        response = self.client.get("/api/weather/3/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_weather3)

    def test_get_weather_temp_lte_30(self):
        """
        Test if the user can get weather data that has temp_c <= 30.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/?temp_c_lte=30")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather2])

    def test_get_weather_temp_gte_40(self):
        """
        Test if the user can get weather data that has temp_c >= 40.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/?temp_c_gte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather3])

    def test_get_weather_by_condition(self):
        """
        Test if the user can get weather data that has condition_text = sunny.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/?condition_text=sunny")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather3])

        response = self.client.get("/api/weather/?condition_text=clear")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather2])

        response = self.client.get("/api/weather/?condition_text=partly cloudy")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather1])

    def test_get_weather_wind_lte_25(self):
        """
        Test if the user can get weather data that has wind_kph <= 25.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/?wind_lte=25")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather1])

    def test_get_weather_wind_gte_25(self):
        """
        Test if the user can get weather data that has wind_kph >= 25.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/?wind_gte=25")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather2, self.expected_weather3])

    def test_get_weather_humidity_lte_40(self):
        """
        Test if the user can get weather data that has humidity <= 40.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/?humidity_lte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather1, self.expected_weather2])

    def test_get_weather_humidity_gte_40(self):
        """
        Test if the user can get weather data that has humidity >= 40.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/?humidity_gte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather3])

    def test_get_weather_cloud_lte_40(self):
        """
        Test if the user can get weather data that has cloud <= 40.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/?cloud_lte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather2])

    def test_get_weather_cloud_gte_40(self):
        """
        Test if the user can get weather data that has cloud >= 40.

        Retrieve a data of specific weather in json format
        """
        response = self.client.get("/api/weather/?cloud_gte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_weather1, self.expected_weather3])


    def test_get_weather_performance(self):
        """
        Test if the API runtime is less than 100ms

        Retrieve a data of weather within 100ms
        """
        start_time = time.time()
        self.client.get("/api/weather/")
        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000
        self.assertLess(response_time_ms, 100, "API response time exceeds 100ms")


class TestDust(BaseTest):
    def test_get_all_dust(self):
        """
        Test if the user can retrieve all data from dust table

        Retrieve a data of all dust in json format
        """
        response = self.client.get("/api/dust/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust1,
                                           self.expected_dust2,
                                           self.expected_dust3])

    def test_get_dust_id(self):
        """
        Test if the user can retrieve a data from dust table by specifying the id.

        Retrieve a data of specific dust in json format
        """
        response = self.client.get("/api/dust/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_dust1)

        response = self.client.get("/api/dust/2/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_dust2)

        response = self.client.get("/api/dust/3/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_dust3)

    def test_get_dust_location(self):
        """
        Test if the user can get dust data that has location as user specified.

        Retrieve a data of specific dust in json format
        """
        response = self.client.get("/api/dust/?location=loc1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust1])

        response = self.client.get("/api/dust/?location=loc2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust2])

        response = self.client.get("/api/dust/?location=loc3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust3])

    def test_get_dust_pm1_lte_15(self):
        """
        Test if the user can get dust data that has pm1 <= 15.

        Retrieve a data of specific dust in json format
        """
        response = self.client.get("/api/dust/?pm1_lte=15")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust1])

    def test_get_dust_pm1_gte_15(self):
        """
        Test if the user can get dust data that has pm1 >= 15.

        Retrieve a data of specific dust in json format
        """
        response = self.client.get("/api/dust/?pm1_gte=15")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust2, self.expected_dust3])

    def test_get_dust_pm2_5_lte_35(self):
        """
        Test if the user can get dust data that has pm2.5 <= 35.

        Retrieve a data of specific dust in json format
        """
        response = self.client.get("/api/dust/?pm2_5_lte=35")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust1])

    def test_get_dust_pm2_5_gte_15(self):
        """
        Test if the user can get dust data that has pm2.5 >= 35.

        Retrieve a data of specific dust in json format
        """
        response = self.client.get("/api/dust/?pm2_5_gte=35")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust2, self.expected_dust3])

    def test_get_dust_pm10_lte_55(self):
        """
        Test if the user can get dust data that has pm10 <= 55.

        Retrieve a data of specific dust in json format
        """
        response = self.client.get("/api/dust/?pm10_lte=55")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust1])

    def test_get_dust_pm10_gte_55(self):
        """
        Test if the user can get dust data that has pm10 >= 55.

        Retrieve a data of specific dust in json format
        """
        response = self.client.get("/api/dust/?pm10_gte=55")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dust2, self.expected_dust3])

    def test_get_dust_performance(self):
        """
        Test if the API runtime is less than 100ms

        Retrieve a data of dust within 100ms
        """
        start_time = time.time()
        self.client.get("/api/dust/")
        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000
        self.assertLess(response_time_ms, 100, "API response time exceeds 100ms")

class TestDustNWeather(BaseTest):
    def test_get_all_dustnweather(self):
        """
        Test if the user can retrieve all data from dustnweather table

        Retrieve a data of all dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather1,
                                           self.expected_dustnweather2,
                                           self.expected_dustnweather3])

    def test_get_dustnweather_id(self):
        """
        Test if the user can retrieve a data from dustnweather table by specifying the id.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_dustnweather1)

        response = self.client.get("/api/dustnweather/2/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_dustnweather2)

        response = self.client.get("/api/dustnweather/3/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_dustnweather3)

    def test_get_dustnweather_location(self):
        """
        Test if the user can get dustnweather data that has location as user specified.

        Retrieve a data of specific dust in json format
        """
        response = self.client.get("/api/dustnweather/?location=loc1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather1])

        response = self.client.get("/api/dustnweather/?location=loc2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather2])

        response = self.client.get("/api/dustnweather/?location=loc3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather3])

    def test_get_dustnweather_pm1_lte_15(self):
        """
        Test if the user can get dustnweather data that has pm1 <= 15.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?pm1_lte=15")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather1])

    def test_get_dustnweather_pm1_gte_15(self):
        """
        Test if the user can get dustnweather data that has pm1 >= 15.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?pm1_gte=15")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather2, self.expected_dustnweather3])

    def test_get_dustnweather_pm2_5_lte_35(self):
        """
        Test if the user can get dustnweather data that has pm2.5 <= 35.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?pm2_5_lte=35")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather1])

    def test_get_dust_pm2_5_gte_15(self):
        """
        Test if the user can get dustnweather data that has pm2.5 >= 35.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?pm2_5_gte=35")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather2, self.expected_dustnweather3])

    def test_get_dustnweather_pm10_lte_55(self):
        """
        Test if the user can get dustnweather data that has pm10 <= 55.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?pm10_lte=55")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather1])

    def test_get_dustnweather_pm10_gte_55(self):
        """
        Test if the user can get dustnweather data that has pm10 >= 55.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?pm10_gte=55")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather2, self.expected_dustnweather3])


    def test_get_dustnweather_temp_lte_30(self):
        """
        Test if the user can get dustnweather data that has temp_c <= 30.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?temp_c_lte=30")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather2])

    def test_get_dustnweather_temp_gte_40(self):
        """
        Test if the user can get dustnweather data that has temp_c >= 40.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?temp_c_gte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather3])

    def test_get_dustnweather_by_condition(self):
        """
        Test if the user can get dustnweather data that has condition_text = sunny.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?condition_text=sunny")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather3])

        response = self.client.get("/api/dustnweather/?condition_text=clear")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather2])

        response = self.client.get("/api/dustnweather/?condition_text=partly cloudy")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather1])

    def test_get_dustnweather_wind_lte_25(self):
        """
        Test if the user can get dustnweather data that has wind_kph <= 25.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?wind_lte=25")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather1])

    def test_get_dustnweather_wind_gte_25(self):
        """
        Test if the user can get dustnweather data that has wind_kph >= 25.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?wind_gte=25")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather2, self.expected_dustnweather3])

    def test_get_dustnweather_humidity_lte_40(self):
        """
        Test if the user can get dustnweather data that has humidity <= 40.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?humidity_lte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather1, self.expected_dustnweather2])

    def test_get_dustnweather_humidity_gte_40(self):
        """
        Test if the user can get dustnweather data that has humidity >= 40.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?humidity_gte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather3])

    def test_get_dustnweather_cloud_lte_40(self):
        """
        Test if the user can get dustnweather data that has cloud <= 40.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?cloud_lte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather2])

    def test_get_dustnweather_cloud_gte_40(self):
        """
        Test if the user can get dustnweather data that has cloud >= 40.

        Retrieve a data of specific dustnweather in json format
        """
        response = self.client.get("/api/dustnweather/?cloud_gte=40")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.expected_dustnweather1, self.expected_dustnweather3])

    def test_get_dustnweather_performance(self):
        """
        Test if the API runtime is less than 100ms

        Retrieve a data of dustnweather within 100ms
        """
        start_time = time.time()
        self.client.get("/api/dustnweather/")
        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000
        self.assertLess(response_time_ms, 100, "API response time exceeds 100ms")
