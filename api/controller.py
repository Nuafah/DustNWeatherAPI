import sys

import pymysql
from dbutils.pooled_db import PooledDB

from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)


def get_bangkok_dust():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("SELECT id, location, pm2_5 FROM bangkok_dust")
        result = [models.DustShort(id, location, pm2_5) for id, location, pm2_5
                  in cs.fetchall()]
    return result


def get_bangkok_dust_details(dust_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, lat, lon, pm1, pm2_5, pm10, location
            FROM bangkok_dust
            WHERE id=%s
            """, [dust_id])
        result = [
            models.DustFull(id, ts, lat, lon, pm1, pm2_5, pm10, location)
            for
            id, ts, lat, lon, pm1, pm2_5, pm10, location
            in cs.fetchall()]
    return result


def get_bangkok_weather():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, temp_c, wind_kph, humidity
            FROM bangkok_weather
            """)
        result = [models.WeatherShort(id, ts, temp_c, wind_kph, humidity) for
                  id, ts, temp_c, wind_kph, humidity
                  in cs.fetchall()]
    return result


def get_bangkok_weather_details(weather_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, name, ts, lat, lon, temp_c, feelslike_c, 
            condition_text, wind_kph, wind_dir, humidity, cloud
            FROM bangkok_weather
            WHERE id=%s
            """, [weather_id])
        result = [
            models.WeatherFull(weather_id, name, ts, lat, lon, temp_c,
                            feelslike_c, condition_text, wind_kph,
                            wind_dir, humidity, cloud)
            for
            weather_id, name, ts, lat, lon, temp_c, feelslike_c,
            condition_text, wind_kph, wind_dir, humidity, cloud
            in cs.fetchall()]
    return result
