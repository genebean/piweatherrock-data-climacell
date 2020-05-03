# piweatherrock-data-climacell

![GitHub](https://img.shields.io/github/license/genebean/python-piweatherrock-data-climacell)
![PyPI](https://img.shields.io/pypi/v/piweatherrock-data-climacell)

This is the source code for the `piweatherrock-data-climacell` Python module. Its purpose is get the data needed for [PiWeatherRock](https://piweatherrock.technicalissues.us) from the [ClimaCell API](https://developer.climacell.co).

## Importing

To use this module you will want to add the following import statement:

```python
from piweatherrock.data_climacell import pwr_data
```

## CLI

This module primarily exists as a component for PiWeatherRock but can also be used on its own. It includes a cli called `pwr-climacell-data` that will return the data usually passed to PiWeatherRock in JSON format. This can be useful to verify what data is being returned by the ClimaCell API.

For example, to see the data associated with Atlanta, GA:

```bash
pwr-climacell-data \
-a $apikey \
--lat 33.753746 \
--lon -84.386330 |jq .
```

Running the command above will produce something similar to this:

```json
{
  "hours": [
    {
      "forecasted_conditions_icon": {
        "value": "clear"
      },
      "forecasted_precipitation_probability": {
        "value": 0,
        "units": "%"
      },
      "forecasted_temp": {
        "value": 72.88,
        "units": "F"
      }
    },
    {
      "forecasted_conditions_icon": {
        "value": "clear"
      },
      "forecasted_precipitation_probability": {
        "value": 0,
        "units": "%"
      },
      "forecasted_temp": {
        "value": 69.98,
        "units": "F"
      }
    },

    [ trimmed ]

    {
      "forecasted_conditions_icon": {
        "value": "clear"
      },
      "forecasted_precipitation_probability": {
        "value": 0,
        "units": "%"
      },
      "forecasted_temp": {
        "value": 77,
        "units": "F"
      }
    }
  ],
  "day0": {
    "current_conditions_string": {
      "value": "clear"
    },
    "current_epa_aqi": {
      "value": 69
    },
    "current_epa_health_concern": {
      "value": "Moderate"
    },
    "current_epa_pm10": {
      "value": 34,
      "units": "µg/m3"
    },
    "current_epa_pm25": {
      "value": 8,
      "units": "µg/m3"
    },
    "current_humidity": {
      "value": 37.5,
      "units": "%"
    },
    "current_pollen_tree": {
      "value": 5,
      "units": "Climacell Pollen Index"
    },
    "current_pollen_weed": {
      "value": null,
      "units": "Climacell Pollen Index"
    },
    "current_pollen_grass": {
      "value": 1,
      "units": "Climacell Pollen Index"
    },
    "current_precipitation_rate": {
      "value": 0,
      "units": "in/hr"
    },
    "current_precipitation_type": {
      "value": "none"
    },
    "current_temp_feels_like": {
      "value": 75.2,
      "units": "F"
    },
    "current_temp_real": {
      "value": 75.2,
      "units": "F"
    },
    "current_wind_direction": {
      "value": 221.06,
      "units": "degrees"
    },
    "current_wind_speed": {
      "value": 4.89,
      "units": "mph"
    },
    "forecasted_conditions_icon": {
      "value": "clear"
    },
    "forecasted_moon_phase": {
      "value": "waxing_gibbous"
    },
    "forecasted_sunrise": {
      "value": "2020-05-02T10:46:55.740Z"
    },
    "forecasted_sunset": {
      "value": "2020-05-03T00:21:50.569Z"
    },
    "forecasted_temp_low": {
      "value": 65.16,
      "units": "F"
    },
    "forecasted_temp_high": {
      "value": 84.58,
      "units": "F"
    },
    "forecasted_time_high_temp": {
      "value": "2020-05-02T20:00:00Z"
    },
    "forecasted_time_low_temp": {
      "value": "2020-05-03T09:00:00Z"
    },
    "forecasted_precipitation_probability": {
      "value": 0,
      "units": "%"
    }
  },
  "day1": {
    "forecasted_conditions_icon": {
      "value": "drizzle"
    },
    "forecasted_moon_phase": {
      "value": "waxing_gibbous"
    },
    "forecasted_sunrise": {
      "value": "2020-05-03T10:45:58.195Z"
    },
    "forecasted_sunset": {
      "value": "2020-05-04T00:22:37.172Z"
    },
    "forecasted_temp_low": {
      "value": 63.77,
      "units": "F"
    },
    "forecasted_temp_high": {
      "value": 86.06,
      "units": "F"
    },
    "forecasted_time_high_temp": {
      "value": "2020-05-03T20:00:00Z"
    },
    "forecasted_time_low_temp": {
      "value": "2020-05-03T11:00:00Z"
    },
    "forecasted_precipitation_probability": {
      "value": 15,
      "units": "%"
    }
  },
  "day2": {
    "forecasted_conditions_icon": {
      "value": "drizzle"
    },

    [ trimmed ]

  },
  "day3": {
    "forecasted_conditions_icon": {
      "value": "rain_light"
    },

    [ trimmed ]

  },
  "observation_time": "2020-05-03T01:34:13.050Z"
}
```
