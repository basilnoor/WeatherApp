# Author: Basil Noor

from tkinter import *
from tkinter import messagebox
import requests


def get_weather(zipcode):
    """Makes a request to get current weather data for user inputted zipcode"""
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&units=imperial&appid={api_key}")

    if weather_data:
        location = weather_data.json()['name']
        weather = f"Forecast: {weather_data.json()['weather'][0]['main']}"
        temp = f"Temp: {round(weather_data.json()['main']['temp'])}"
        temp_min = f"Min: {round(weather_data.json()['main']['temp_min'])}"
        temp_max = f"Max: {round(weather_data.json()['main']['temp_max'])}"
        icon = weather_data.json()['weather'][0]['icon']
        final = (location, icon, weather, temp, temp_min, temp_max)
        return final
    else:
        return None


def search():
    """Takes data from user input and requests from API to replace labels with current weather info"""
    zipcode = zipcode_text.get()
    weather = get_weather(zipcode)

    if weather:
        location_label["text"] = f"{weather[0]}"
        weather_label["text"] = weather[2]
        temp_label["text"] = f"{weather[3]}°F"
        temp_min_label["text"] = f"{weather[4]}°F"
        temp_max_label["text"] = f"{weather[5]}°F"

    else:
        messagebox.showerror("Error", f"Cannot Find Zipcode {zipcode}")


# API key allowing us access to weather information and general configuration
api_key = "insert_api_key"

# Initializing Tkinter
app = Tk()
app.title("Weather App")
app.geometry('450x200')

# All labels/buttons
zipcode_text = StringVar()
zipcode_entry = Entry(app, textvariable=zipcode_text)
zipcode_entry.pack()

search_button = Button(app, text="Search Weather", width=12, command=search)
search_button.pack()

location_label = Label(app, text="Please enter an Zipcode (U.S.A)", font=("bold", 20))
location_label.pack()

weather_label = Label(app, text="Current Forecast")
weather_label.pack()

temp_label = Label(app, text="Current Temperature")
temp_label.pack()

temp_min_label = Label(app, text="Minimum Temperature")
temp_min_label.pack()

temp_max_label = Label(app, text="Maximum Temperature")
temp_max_label.pack()

button_quit = Button(app, text="Quit", width=8, command=app.destroy)
button_quit.pack()


app.mainloop()
