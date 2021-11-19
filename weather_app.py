import requests

# API key allowing us access to weather information
api_key = "5e21987cfd42ffaa803de02a742e990a"

user_input = input("Enter Zipcode (USA): ")

# Request which allows us you fetch the weather information based on zipcode.
# Uses user input and converts units to imperial.
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={user_input},us&units=imperial&appid={api_key}")

if weather_data.json()['cod'] == '404':
    print("Not A Proper Zipcode")
else:
    location = weather_data.json()['name']
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    temp_min = round(weather_data.json()['main']['temp_min'])
    temp_max = round(weather_data.json()['main']['temp_max'])
    print()
    print(f"The following is weather information for {location}, zipcode {user_input}:")
    print()
    print(f"Current forecast: {weather}")
    print(f"Current temperature is: {temp}°F")
    print(f"Minimum temperature of: {temp_min}°F")
    print(f"Maximum temperature: {temp_max}°F")
