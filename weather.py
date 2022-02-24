import pprint, requests

class YahooWeatherForecast:

    # ИНИЦИАЛИЗАЦИЯ КЛАССА
    def __init__(self):
        self._city_cache = {}

    # СВЕДЕНИЯ О ПОГОДЕ
    def get(self, city):

        if city in self._city_cache:
            return self._city_cache[city]

        # ЯХУ ПОГОДА, ИСХОДНИКИ НА РАПИДЕ
        url = "https://yahoo-weather5.p.rapidapi.com/weather"
        print('sending HTTP request')
        querystring = {"location":f"{city}","format":"json","u":"c"}

        headers = {
            'x-rapidapi-host': "yahoo-weather5.p.rapidapi.com",
            'x-rapidapi-key': "МОЙ АПИ"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()
        current_city = response['location']['city']
        weather = response['current_observation']['condition']['temperature']

        current_weather = 'Город: ' + current_city + '\nТемпература: ' + str(weather)

        self._city_cache[city] = current_weather
        return current_weather

# ИНФОРМАЦИЯ О ГОРОДЕ
class CityInfo:

    def __init__(self, city, weather_forecast = None):
        self.city = city
        self._weather_forecast = weather_forecast or YahooWeatherForecast

    def weather_forecast(self):
        print(self._weather_forecast.get(self.city))

def _main():
    weather_forecast = YahooWeatherForecast()
    city_info = CityInfo("Moscow", weather_forecast = weather_forecast)
    forecast = city_info.weather_forecast()

if __name__ == "__main__":
    _main()
