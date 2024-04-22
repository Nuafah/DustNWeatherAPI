# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dust_full import DustFull  # noqa: E501
from swagger_server.models.dust_short import DustShort  # noqa: E501
from swagger_server.models.weather_full import WeatherFull  # noqa: E501
from swagger_server.models.weather_short import WeatherShort  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_bangkok_dust(self):
        """Test case for controller_get_bangkok_dust

        Returns a list of bangkok dust.
        """
        response = self.client.open(
            '/bangkok_dust',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_bangkok_dust_details(self):
        """Test case for controller_get_bangkok_dust_details

        Returns complete details of the specified id
        """
        response = self.client.open(
            '/bangkok_dust/{dust_id}'.format(dust_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_bangkok_weather(self):
        """Test case for controller_get_bangkok_weather

        Returns a list of bangkok weather.
        """
        response = self.client.open(
            '/bangkok_weather',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_bangkok_weather_details(self):
        """Test case for controller_get_bangkok_weather_details

        Returns complete details of bangkok weather.
        """
        response = self.client.open(
            '/bangkok_weather/{weather_id}'.format(weather_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
