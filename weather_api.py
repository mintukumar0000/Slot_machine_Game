import requests,json
api_key = '6ddd1c99ab80290bdb6ea0f716e4c8d2'
user_input = input("Enter the city: ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json() ['cod'] == '404':
    print("No city found")

else:
    weather = weather_data.json()['weather'][0]['main']# identity the weather is clean or rain, clouds
    temp = weather_data.json()['main']['temp']

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temp in {user_input} is: {temp}°F")    