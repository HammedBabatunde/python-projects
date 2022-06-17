import requests



def get_weather():

    api_Key = '0a8cebb64361c4c657c1fb4405c323fd'
    weathers = {}

    while True:
            
        city_name = input('Enter a city: ')
        base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_Key}'

        weather_data = requests.get(base_url).json()
        current_weather = weather_data['weather'][0]['description']

        weathers[city_name] = current_weather

        get_another = input('Do you want to get the weather of another city (Yes or No): ')

        if get_another == 'Yes':
            continue
        elif get_another == 'No':
            break
            
    return weathers


def print_weather(weather_data):
    for city, weather in weather_data.items():
        print(f'{city} current weather condition is {weather}')
    
    return True


# print_weather(get_weather()) ## method 1
weather_data = get_weather()
print_weather(weather_data) 