# DustNWeatherAPI
It looks like you're describing a project called DustNWeatherAPI that collects data on air quality using a dust sensor [PMS7003](https://github.com/teusH/MySense/blob/master/docs/pms7003.md) and weather information from the [WeatherAPI](https://www.weatherapi.com/api-explorer.aspx). Then, it visualizes and integrates this data.

For visualization, the application displays PM1, PM2.5, and PM10 data collected between April 20, 2024, and May 10, 2024, along with the average temperature, wind speed, humidity, and cloud cover during that period.

Regarding the API, the application offers endpoints to retrieve information on dust and weather, with filtering options provided using Django Rest Framework.
## Install instructions
Please configure the `sample.env` file before proceeding with the installation.

Please install chart js
```
npm install chart.js
```
And all requirements
```
pip install -r requirements
```
## How to run

1. To run the server

```
python manage.py runserver
```

2. To access the app at http://localhost:8000

3. To deactivate the virtual environment

```
deactivate
```

## Team member
Kanisorn KANOKRATANA 6510545284 Software and Knowledge Engineering student
Yasatsawin KULDEJTITIPUN 6510545705 Software and Knowledge Engineering student
