import unittest
from unittest.mock import patch
import forecast

class TestWeatherForecastTool(unittest.TestCase):
    @patch("forecast.r.get")
    def test_get_weather(self, mock_get):
        city = "New York"
        expected_url = f"http://api.weatherapi.com/v1/forecast.json?key={forecast.apikey}&q={city}&days=3"
        expected_data = {
            "forecast": {
                "forecastday": [
                    {
                        "day": {
                            "maxtemp_c": 28,
                            "maxtemp_f": 82,
                            "mintemp_c": 25,
                            "mintemp_f": 77,
                            "condition": {"text": "Sunny"},
                            "avghumidity": 60,
                            "daily_chance_of_rain": "10%",
                            "totalprecip_mm": 5
                        },
                        "astro": {
                            "sunrise": "06:00",
                            "sunset": "18:00",
                            "moonrise": "12:00",
                            "moonset": "00:00"
                        }
                    }
                ]
            },
            "location": {
                "name": "New York",
                "region": "New York",
                "country": "United States"
            }
        }
        mock_get.return_value.json.return_value = expected_data

        result = forecast.getWeather(city)

        mock_get.assert_called_with(expected_url)
        self.assertEqual(mock_get.return_value.json.call_count, 1)
        args, kwargs = mock_get.return_value.json.call_args
        self.assertEqual(result, expected_data)

if __name__ == '__main__':
    unittest.main()
