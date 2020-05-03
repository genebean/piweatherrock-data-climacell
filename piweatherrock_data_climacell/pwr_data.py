from datetime import datetime as datetime
from datetime import timedelta as timedelta
import json
import requests
import sys


class Forecast:
    """
    A class used to represent a forecast from ClimaCell.

    A forecast object contains all the data needed by PiWeatherRock.
    This is accomplished by taking the data from the ClimaCell API
    fitting it into a "forecast_data" object that is consumed by the
    main application.
    """

    def __init__(self, apikey, latitude, longitude, units='us'):
        """
        Parameters
        ----------
        apikey : str
            A user's API key for ClimaCell
        latitude : float
            The latitude of the location for which a user whishes to
            retrieve a forecast.
        longitude : float
            The longitude of the location for which a user whishes to
            retrieve a forecast.
        units : str, optional
            The units that the forecast should use (default is 'us')
        """

        self.apikey = apikey
        self.latitude = latitude
        self.longitude = longitude
        self.units = units
        self.forecast_data = {
            # Each hours element is a hash like this:
            # {
            #     'forecasted_conditions_icon': {
            #         'value': None,
            #     },
            #     'forecasted_precipitation_probability': {
            #         'value': None,
            #         'units': None,
            #     },
            #     'forecasted_temp': {
            #         'value': None,
            #     },
            # }
            'hours': [],
            'day0': {
                'current_conditions_string': {
                    'value': None,
                },
                'current_epa_aqi': {
                    'value': None,
                    'units': None,
                },
                'current_epa_health_concern': {
                    'value': None,
                },
                'current_epa_pm10': {
                    'value': None,
                    'units': None,
                },
                'current_epa_pm25': {
                    'value': None,
                    'units': None,
                },
                'current_humidity': {
                    'value': None,
                    'units': None,
                },
                'current_pollen_tree': {
                    'value': None,
                    'units': None,
                },
                'current_pollen_weed': {
                    'value': None,
                    'units': None,
                },
                'current_pollen_grass': {
                    'value': None,
                    'units': None,
                },
                'current_precipitation_rate': {
                    'value': None,
                    'units': None,
                },
                'current_precipitation_type': {
                    'value': None,
                },
                'current_temp_feels_like': {
                    'value': None,
                    'units': None,
                },
                'current_temp_real': {
                    'value': None,
                    'units': None,
                },
                'current_wind_direction': {
                    'value': None,
                    'units': None,
                },
                'current_wind_speed': {
                    'value': None,
                    'units': None,
                },
                'forecasted_conditions_icon': {
                    'value': None,
                },
                'forecasted_moon_phase': {
                    'value': None,
                },
                'forecasted_sunrise': {
                    'value': None,
                },
                'forecasted_sunset': {
                    'value': None,
                },
                'forecasted_temp_low': {
                    'value': None,
                    'units': None,
                },
                'forecasted_temp_high': {
                    'value': None,
                    'units': None,
                },
                'forecasted_time_high_temp': {
                    'value': None,
                },
                'forecasted_time_low_temp': {
                    'value': None,
                },
                'forecasted_precipitation_probability': {
                    'value': None,
                    'units': None,
                },
            },
            'day1': {
                'forecasted_conditions_icon': {
                    'value': None,
                },
                'forecasted_moon_phase': {
                    'value': None,
                },
                'forecasted_sunrise': {
                    'value': None,
                },
                'forecasted_sunset': {
                    'value': None,
                },
                'forecasted_temp_low': {
                    'value': None,
                    'units': None,
                },
                'forecasted_temp_high': {
                    'value': None,
                    'units': None,
                },
                'forecasted_time_high_temp': {
                    'value': None,
                },
                'forecasted_time_low_temp': {
                    'value': None,
                },
                'forecasted_precipitation_probability': {
                    'value': None,
                    'units': None,
                },
            },
            'day2': {
                'forecasted_conditions_icon': {
                    'value': None,
                },
                'forecasted_moon_phase': {
                    'value': None,
                },
                'forecasted_sunrise': {
                    'value': None,
                },
                'forecasted_sunset': {
                    'value': None,
                },
                'forecasted_temp_low': {
                    'value': None,
                    'units': None,
                },
                'forecasted_temp_high': {
                    'value': None,
                    'units': None,
                },
                'forecasted_time_high_temp': {
                    'value': None,
                },
                'forecasted_time_low_temp': {
                    'value': None,
                },
                'forecasted_precipitation_probability': {
                    'value': None,
                    'units': None,
                },
            },
            'day3': {
                'forecasted_conditions_icon': {
                    'value': None,
                },
                'forecasted_moon_phase': {
                    'value': None,
                },
                'forecasted_sunrise': {
                    'value': None,
                },
                'forecasted_sunset': {
                    'value': None,
                },
                'forecasted_temp_low': {
                    'value': None,
                    'units': None,
                },
                'forecasted_temp_high': {
                    'value': None,
                    'units': None,
                },
                'forecasted_time_high_temp': {
                    'value': None,
                },
                'forecasted_time_low_temp': {
                    'value': None,
                },
                'forecasted_precipitation_probability': {
                    'value': None,
                    'units': None,
                },
            },
            'observation_time': {
                'value': None,
            },
        }

    def get_forecast(self):
        """
        Update self.forecast_data with information from ClimaCell
        """

        # Currently, three api calls are needed to collect the data used
        # in PiWeatherRock. ClimaCell says they are working on a way to
        # get this same data in a single call.
        realtime = self.__get_realtime_forecast()
        hourly = self.__get_hourly_forecast()
        daily = self.__get_daily_forecast()

        # Fill in data from the realtime endpoint
        self.forecast_data['day0']['current_temp_real'] = realtime['temp']
        self.forecast_data['day0']['current_temp_feels_like'] = realtime['feels_like']
        self.forecast_data['day0']['current_wind_speed'] = realtime['wind_speed']
        self.forecast_data['day0']['current_humidity'] = realtime['humidity']
        self.forecast_data['day0']['current_wind_direction'] = realtime['wind_direction']
        self.forecast_data['day0']['current_precipitation_rate'] = realtime['precipitation']
        self.forecast_data['day0']['current_precipitation_type'] = realtime['precipitation_type']
        self.forecast_data['day0']['forecasted_sunrise'] = realtime['sunrise']
        self.forecast_data['day0']['forecasted_sunset'] = realtime['sunset']
        self.forecast_data['day0']['forecasted_moon_phase'] = realtime['moon_phase']
        self.forecast_data['day0']['current_conditions_string'] = realtime['weather_code']
        self.forecast_data['day0']['forecasted_conditions_icon'] = realtime['weather_code']
        self.forecast_data['day0']['current_epa_aqi'] = realtime['epa_aqi']
        self.forecast_data['day0']['current_epa_pm25'] = realtime['pm25']
        self.forecast_data['day0']['current_epa_pm10'] = realtime['pm10']
        self.forecast_data['day0']['current_epa_health_concern'] = realtime['epa_health_concern']
        self.forecast_data['day0']['current_pollen_tree'] = realtime['pollen_tree']
        self.forecast_data['day0']['current_pollen_weed'] = realtime['pollen_weed']
        self.forecast_data['day0']['current_pollen_grass'] = realtime['pollen_grass']
        self.forecast_data['observation_time'] = realtime['observation_time']['value']

        # Fill in data from the hourly endpoint
        for i in range(len(hourly)):
            data = {
                'forecasted_conditions_icon': {
                    'value': None,
                },
                'forecasted_precipitation_probability': {
                    'value': None,
                    'units': None,
                },
                'forecasted_temp': {
                    'value': None,
                },
            }
            data['forecasted_conditions_icon'] = hourly[i]['weather_code']
            data['forecasted_temp'] = hourly[i]['temp']
            data['forecasted_precipitation_probability'] = hourly[i]['precipitation_probability']

            # On first run there won't yet be any elements in the array of
            # hours so we catch that exception and append the element to it.
            try:
                self.forecast_data['hours'][i] = data
            except IndexError:
                self.forecast_data['hours'].append(data)

        # Fill in data from the daily endpoint
        for i in range(len(daily)):
            self.forecast_data['day' +
                               str(i)]['forecasted_conditions_icon'] = daily[i]['weather_code']
            self.forecast_data['day' +
                               str(i)]['forecasted_moon_phase'] = daily[i]['moon_phase']
            self.forecast_data['day' +
                               str(i)]['forecasted_sunrise'] = daily[i]['sunrise']
            self.forecast_data['day' +
                               str(i)]['forecasted_sunset'] = daily[i]['sunset']
            self.forecast_data['day' +
                               str(i)]['forecasted_temp_low'] = daily[i]['temp'][0]['min']
            self.forecast_data['day' + str(
                i)]['forecasted_time_low_temp']['value'] = daily[i]['temp'][0]['observation_time']
            self.forecast_data['day' +
                               str(i)]['forecasted_temp_high'] = daily[i]['temp'][1]['max']
            self.forecast_data['day' + str(
                i)]['forecasted_time_high_temp']['value'] = daily[i]['temp'][1]['observation_time']
            self.forecast_data['day' + str(
                i)]['forecasted_precipitation_probability'] = daily[i]['precipitation_probability']

        return self.forecast_data

    def print_forecast_data(self):
        """Print out a JSON representation of the forecast_data object"""

        print(json.dumps(self.forecast_data))

    def __get_realtime_forecast(self):
        """
        Helper method to simplify querying the realtime endpoint
        """

        return self.__query_api('realtime')

    def __get_hourly_forecast(self):
        """
        Helper method to simplify querying the hourly endpoint
        """

        return self.__query_api('hourly')

    def __get_daily_forecast(self):
        """
        Helper method to simplify querying the daily endpoint
        """

        return self.__query_api('daily')

    def __query_api(self, endpoint):
        """
        Reach out to the ClimaCell api and get the needed data.

        Return the results as a JSON object.
        """

        if endpoint == 'realtime':
            url = "https://api.climacell.co/v3/weather/" + endpoint
        else:
            url = "https://api.climacell.co/v3/weather/forecast/" + endpoint

        fileds_string = self.__get_fields(endpoint)
        querystring = {
            "lat": self.latitude,
            "lon": self.longitude,
            "unit_system": self.units,
            "apikey": self.apikey,
            "fields": fileds_string,
        }

        if endpoint == 'hourly':
            now = datetime.now().utcnow()
            now_plus_one_day = timedelta(hours=24)
            end_time = (now + now_plus_one_day).isoformat() + 'Z'
            querystring['end_time'] = end_time
        elif endpoint == 'daily':
            now = datetime.now().utcnow()
            now_plus_three_days = timedelta(days=3)
            end_time = (now + now_plus_three_days).isoformat() + 'Z'
            querystring['end_time'] = end_time

        response = requests.request("GET", url, params=querystring)

        return response.json()

    def __get_fields(self, endpoint):
        """
        Returns a string of all the fields for a ClimaCell weather endpoint.
        """

        # TODO: Implement a way to append units to select fields based
        # on a map of chosen display language to desired unit.
        #
        # https://developer.climacell.co/v3/reference#data-layers says:
        # Regardless of the units chosen in the request, you may change
        # the units of each data layer by adding the relevant suffix.
        # For example, if you request /daily data in SI units, you can
        # add the field precipitation:in/hr thereby overriding the
        # original units (mm/hr).

        common_fields = [
            'feels_like',
            'humidity',
            'moon_phase',
            'precipitation',
            'sunrise',
            'sunset',
            'temp',
            'weather_code',
            'wind_direction',
            'wind_speed',
        ]

        if endpoint == 'realtime':
            additional_fields = [
                'epa_aqi',
                'epa_health_concern',
                'pm10',
                'pm25',
                'pollen_grass',
                'pollen_tree',
                'pollen_weed',
                'precipitation_type',
            ]
        elif endpoint == 'hourly':
            additional_fields = [
                'epa_aqi',
                'epa_health_concern',
                'pm10',
                'pm25',
                'pollen_grass',
                'pollen_tree',
                'pollen_weed',
                'precipitation_probability',
                'precipitation_type',
            ]
        elif endpoint == 'daily':
            additional_fields = [
                'precipitation_accumulation',
                'precipitation_probability',
            ]
        else:
            print('invaid endpoint requested')
            sys.exit(1)

        return ",".join(common_fields + additional_fields)
