import requests
from config import key


def get_weather(key, city):
    try:
        # Создаем запрос и обращаемся с нашими данными на сервер.
        response = requests.get(f"https://api.weatherapi.com/v1/forecast.json?key={key}&q={city}&days=3")
        # Преобразуем данные в JSON формат. Проверяем ответ от сервера.
        if response.status_code == 200:
            weather = response.json()
            return weather
        # В случае некорректного ответа от сервера пишем код ошибки и вызываем функцию выбора города.
        else:
            print(f'Не удалось получить данные о погоде. Код ошибки: {response.status_code}')
    # Обрабатываем ошибки.
    except:
        raise Exception('Ошибка при получении погоды. Проверьте правильность ввода города.')


# Записываем результат функции в глобальную переменную.


# Получаем температуру из JSON.
def get_temp(weather):
    temp = weather['current'].get('temp_c')
    feelslike_temp = weather['current'].get('feelslike_c')
    return temp, feelslike_temp


# Получаем скорость ветра из JSON и переводим ее в метры в секунду.
def get_wind(weather):
    wind = weather['current'].get('wind_kph')
    wind_mps = wind // 3.6
    return wind_mps


# Получаем порывы ветра из JSON и переводим их в метры в секунду.
def get_gust(weather):
    gust = weather['current'].get('gust_kph')
    gust_mps = gust // 3.6
    return gust_mps


# Получаем влажность воздуха.
def get_humidity(weather):
    humidity = weather['current'].get('humidity')
    return humidity


# Получаем облачность.
def get_cloud(weather):
    cloud = weather['current'].get('cloud')
    return cloud


# Получаем количество осадков.
def get_precip(weather):
    precip_mm = weather['current'].get('precip_mm')
    return precip_mm


# Проверяем есть ли в данный момент дождь.
def get_rain(weather):
    precip_mm = get_precip(weather)
    # Проверяем есть ли в данный момент дождь.
    if precip_mm > 0:
        rain = 'В данный момент идет дождь.'
        return rain
    else:
        rain = 'В данный момент нет дождя'
        return rain


# Получаем текущее направление ветра.
def get_wind_dir(weather):
    wind_dir = weather['current'].get('wind_dir')
    return wind_dir


# Получаем дату последнего обновления данных.
def get_last_update(weather):
    last_update = weather['current'].get('last_updated')
    return last_update


# Высчитываем индекс термического комфорта.
def get_index(weather):
    temp = get_temp(weather)[0]
    humidity = get_humidity(weather)
    wind_mps = get_wind(weather)
    heat_index = 37 - (37 - temp) / (
            0.68 - 0.0014 * humidity + 1 / (1.76 + 1.4 * wind_mps ** 0.75)) - 0.29 * temp * (
                         1 - humidity / 100)
    return heat_index


# Получаем максимальную и минимальную температуру в течении дня.
def get_forecast_temp(weather):
    maxtemp = weather['forecast']['forecastday'][0]['day']['maxtemp_c']
    mintemp = weather['forecast']['forecastday'][0]['day']['mintemp_c']
    return maxtemp, mintemp


# Получаем среднюю температуру в течении дня.
def get_average_temp(weather):
    avgtemp = weather['forecast']['forecastday'][0]['day']['avgtemp_c']
    return avgtemp


# Получаем максимальную скорость ветра в течении дня.
def get_max_wind(weather):
    max_wind_kph = weather['forecast']['forecastday'][0]['day']['maxwind_kph']
    max_wind = max_wind_kph // 3.6
    return max_wind


# Получаем общее количество осадков в течении дня.
def get_total_precip(weather):
    total_precip = weather['forecast']['forecastday'][0]['day']['totalprecip_mm']
    return total_precip


# Получаем вероятность дождя в течении дня.
def get_daily_chance_of_rain(weather):
    daily_chance_of_rain = weather['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
    return daily_chance_of_rain


# Получаем время восхода солнца.
def get_sunrise(weather):
    sunrise = weather['forecast']['forecastday'][0]['astro']['sunrise']
    return sunrise


# Получаем время захода солнца.
def get_sunset(weather):
    sunset = weather['forecast']['forecastday'][0]['astro']['sunset']
    return sunset


# Получаем температуру в 00:00 часов.
def get_temp_midnight(weather):
    midnight_temp = weather['forecast']['forecastday'][0]['hour'][0]['temp_c']
    return midnight_temp


# Получаем температуру в 09:00 часов.
def get_temp_morning(weather):
    morning_temp = weather['forecast']['forecastday'][0]['hour'][9]['temp_c']
    return morning_temp


# Получаем температуру в 12:00 часов.
def get_temp_day(weather):
    day_temp = weather['forecast']['forecastday'][0]['hour'][12]['temp_c']
    return day_temp


# Получаем температуру в 18:00 часов.
def get_temp_evening(weather):
    evening_temp = weather['forecast']['forecastday'][0]['hour'][18]['temp_c']
    return evening_temp


# Получаем скорость ветра в 00:00 часов.
def get_wind_midnight(weather):
    midnight_wind_kph = weather['forecast']['forecastday'][0]['hour'][0]['wind_kph']
    midnight_wind = midnight_wind_kph // 3.6
    return midnight_wind


# Получаем скорость ветра в 09:00 часов.
def get_wind_morning(weather):
    morning_wind_kph = weather['forecast']['forecastday'][0]['hour'][9]['wind_kph']
    morning_wind = morning_wind_kph // 3.6
    return morning_wind


# Получаем скорость ветра в 12:00 часов.
def get_wind_day(weather):
    day_wind_kph = weather['forecast']['forecastday'][0]['hour'][12]['wind_kph']
    day_wind = day_wind_kph // 3.6
    return day_wind


# Получаем скорость ветра в 18:00 часов.
def get_wind_evening(weather):
    evening_wind_kph = weather['forecast']['forecastday'][0]['hour'][18]['wind_kph']
    evening_wind = evening_wind_kph // 3.6
    return evening_wind


# Получаем текущую дату.
def get_current_day(weather):
    current_date = weather['forecast']['forecastday'][0]['date']
    return current_date


def get_first_day(weather):
    first_date = weather['forecast']['forecastday'][0]['date']
    return first_date


def get_first_day_avg_temp(weather):
    avg_temp = weather['forecast']['forecastday'][0]['day']['avgtemp_c']
    return avg_temp


def get_first_day_max_wind(weather):
    max_wind_kph = weather['forecast']['forecastday'][0]['day']['maxwind_kph']
    max_wind = max_wind_kph // 3.6
    return max_wind


def get_first_day_totalprecip(weather):
    total_precip = weather['forecast']['forecastday'][0]['day']['totalprecip_mm']
    return total_precip


def get_first_day_avg_humidity(weather):
    avg_humidity = weather['forecast']['forecastday'][0]['day']['avghumidity']
    return avg_humidity


def get_first_day_chance_of_rain(weather):
    chance_of_rain = weather['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
    return chance_of_rain


def get_second_day(weather):
    second_date = weather['forecast']['forecastday'][1]['date']
    return second_date


def get_second_day_avg_temp(weather):
    avg_temp = weather['forecast']['forecastday'][1]['day']['avgtemp_c']
    return avg_temp


def get_second_day_max_wind(weather):
    max_wind_kph = weather['forecast']['forecastday'][1]['day']['maxwind_kph']
    max_wind = max_wind_kph // 3.6
    return max_wind


def get_second_day_totalprecip(weather):
    total_precip = weather['forecast']['forecastday'][1]['day']['totalprecip_mm']
    return total_precip


def get_second_day_avg_humidity(weather):
    avg_humidity = weather['forecast']['forecastday'][1]['day']['avghumidity']
    return avg_humidity


def get_second_day_chance_of_rain(weather):
    chance_of_rain = weather['forecast']['forecastday'][1]['day']['daily_chance_of_rain']
    return chance_of_rain


def get_third_day(weather):
    third_date = weather['forecast']['forecastday'][2]['date']
    return third_date


def get_third_day_avg_temp(weather):
    avg_temp = weather['forecast']['forecastday'][2]['day']['avgtemp_c']
    return avg_temp


def get_third_day_max_wind(weather):
    max_wind_kph = weather['forecast']['forecastday'][2]['day']['maxwind_kph']
    max_wind = max_wind_kph // 3.6
    return max_wind


def get_third_day_totalprecip(weather):
    total_precip = weather['forecast']['forecastday'][2]['day']['totalprecip_mm']
    return total_precip


def get_third_day_avg_humidity(weather):
    avg_humidity = weather['forecast']['forecastday'][2]['day']['avghumidity']
    return avg_humidity


def get_third_day_chance_of_rain(weather):
    chance_of_rain = weather['forecast']['forecastday'][2]['day']['daily_chance_of_rain']
    return chance_of_rain


def get_name_city(weather):
    name_city = weather['location']['name']
    return name_city


# Функция для текущего прогноза погоды.
def send_result_current(weather):
    return f'''-----------------------------------------------------------------------
    ⏰ Данные погоды на: {get_last_update(weather)}
    🏙 Для города: {get_name_city(weather)}
    -----------------------------------------------------------------------
    🌡 Температура воздуха: {get_temp(weather)[0]} градусов. Ощущается как: {get_temp(weather)[1]} градусов.
    💨 Скорость ветра: {get_wind(weather)} м/с. Порывы до: {get_gust(weather)} м/с.
    💦 Влажность воздуха: {get_humidity(weather)}%
    ☁️ Облачность: {get_cloud(weather)}%
    🧭 Направление ветра: {get_wind_dir(weather)}
    ☔️ Количество осадков: {get_precip(weather)} мм.
    {get_rain(weather)}
    -----------------------------------------------------------------------
    Индекс термического комфорта: {get_index(weather)}
    -----------------------------------------------------------------------'''


# Функция для отправки прогноза погоды на целый день.
def send_result_forecastday(weather):
    return f'''-----------------------------------------------------------------------
    ⏰ Данные погоды для: {get_current_day(weather)}
    🏙 Для города: {get_name_city(weather)}
    -----------------------------------------------------------------------
    🌡 Температура воздуха в 00:00: {get_temp_midnight(weather)} градусов.
    💨 Скорость ветра в 00:00: {get_wind_midnight(weather)} м/с.
    -----------------------------------------------------------------------
    🌡 Температура воздуха в 09:00: {get_temp_morning(weather)} градусов.
    💨 Скорость ветра в 09:00: {get_wind_morning(weather)} м/с.
    -----------------------------------------------------------------------
    🌡 Температура воздуха в 12:00: {get_temp_day(weather)} градусов.
    💨 Скорость ветра в 12:00: {get_wind_day(weather)} м/с.
    -----------------------------------------------------------------------
    🌡 Температура воздуха в 18:00: {get_temp_evening(weather)} градусов.
    💨 Скорость ветра в 18:00: {get_wind_evening(weather)} м/с.
    -----------------------------------------------------------------------
    🌡 Максимальная температура воздуха в течении дня: {get_forecast_temp(weather)[0]} градусов.
    🌡 Минимальная температура воздуха в течении дня: {get_forecast_temp(weather)[1]} градусов.
    🌡 Средняя температура воздуха в течении дня: {get_average_temp(weather)} градусов.
    💨 Максимальная скорость ветра: {get_max_wind(weather)} м/с.
    💦 Количество осадков за день: {get_total_precip(weather)} мм.
    ☔️ Вероятность дождя: {get_daily_chance_of_rain(weather)}%
    -----------------------------------------------------------------------
    🌅 Восход: {get_sunrise(weather)}
    🌇 Закат: {get_sunset(weather)}
    -----------------------------------------------------------------------'''


def send_result_forecast_three_days(weather):
    return f'''
    🏙 Для города: {get_name_city(weather)}
    -----------------------------------------------------------------------
    ⏰ Данные погоды на: {get_first_day(weather)}
    🌡 Средняя температура в течении дня: {get_first_day_avg_temp(weather)} градусов.
    💨 Максимальная скорость ветра: {get_first_day_max_wind(weather)} м/с.
    ☔️ Количество осадков за день: {get_first_day_totalprecip(weather)} мм.
    💦 Средняя влажность: {get_first_day_avg_humidity(weather)}%
    ☔️ Вероятность дождя: {get_first_day_chance_of_rain(weather)}%
    -----------------------------------------------------------------------
    ⏰ Данные погоды на: {get_second_day(weather)}
    🌡 Средняя температура в течении дня: {get_second_day_avg_temp(weather)} градусов.
    💨 Максимальная скорость ветра: {get_second_day_max_wind(weather)} м/с.
    ☔️ Количество осадков за день: {get_second_day_totalprecip(weather)} мм.
    💦 Средняя влажность: {get_second_day_avg_humidity(weather)}%
    ☔️ Вероятность дождя: {get_second_day_chance_of_rain(weather)}%
    -----------------------------------------------------------------------
    ⏰ Данные погоды на: {get_third_day(weather)}
    🌡 Средняя температура в течении дня: {get_third_day_avg_temp(weather)} градусов.
    💨 Максимальная скорость ветра: {get_third_day_max_wind(weather)} м/с.
    ☔️ Количество осадков за день: {get_third_day_totalprecip(weather)} мм.
    💦 Средняя влажность: {get_third_day_avg_humidity(weather)}%
    ☔️ Вероятность дождя: {get_third_day_chance_of_rain(weather)}%
    -----------------------------------------------------------------------'''


def start_weather_current(city):
    return send_result_current(get_weather(key, city))


def start_weather_forecast(city):
    return send_result_forecastday(get_weather(key, city))


def start_weather_three_days(city):
    return send_result_forecast_three_days(get_weather(key, city))