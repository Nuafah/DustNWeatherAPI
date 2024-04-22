import connexion
import six

from swagger_server.models.dust_full import DustFull  # noqa: E501
from swagger_server.models.dust_short import DustShort  # noqa: E501
from swagger_server.models.weather_full import WeatherFull  # noqa: E501
from swagger_server.models.weather_short import WeatherShort  # noqa: E501
from swagger_server import util


def controller_get_bangkok_dust():  # noqa: E501
    """Returns a list of bangkok dust.

     # noqa: E501


    :rtype: List[DustShort]
    """
    return 'do some magic!'


def controller_get_bangkok_dust_details(dust_id):  # noqa: E501
    """Returns complete details of the specified id

     # noqa: E501

    :param dust_id: 
    :type dust_id: int

    :rtype: DustFull
    """
    return 'do some magic!'


def controller_get_bangkok_weather():  # noqa: E501
    """Returns a list of bangkok weather.

     # noqa: E501


    :rtype: List[WeatherShort]
    """
    return 'do some magic!'


def controller_get_bangkok_weather_details(weather_id):  # noqa: E501
    """Returns complete details of bangkok weather.

     # noqa: E501

    :param weather_id: 
    :type weather_id: int

    :rtype: List[WeatherFull]
    """
    return 'do some magic!'
