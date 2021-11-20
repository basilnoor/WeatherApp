from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from configparser import ConfigParser
import requests


def get_weather(zipcode):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&units=imperial&appid={api_key}")

    if weather_data:
        location = weather_data.json()['name']
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        temp_min = round(weather_data.json()['main']['temp_min'])
        temp_max = round(weather_data.json()['main']['temp_max'])
        icon = weather_data.json()['weather'][0]['icon']
        final = (location, icon, weather, temp, temp_min, temp_max)
        return final
    else:
        return None


def search():
    zipcode = zipcode_text.get()
    weather = get_weather(zipcode)
    if weather:
        location_label["text"] = f"{weather[0]}"

        image = ImageTk.PhotoImage(file="01d.png")
        icon = Label(app)
        icon.place(x=0, y=0)
        icon.config(image=image)

        weather_label["text"] = weather[2]
        temp_label["text"] = f"{weather[3]}°F"
        temp_min_label["text"] = f"{weather[4]}°F"
        temp_max_label["text"] = f"{weather[5]}°F"
    else:
        messagebox.showerror("Error", f"Cannot Find Zipcode {zipcode}")


# API key allowing us access to weather information
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = "5e21987cfd42ffaa803de02a742e990a"

app = Tk()
app.title("Weather App")
app.geometry('500x350')

zipcode_text = StringVar()
zipcode_entry = Entry(app, textvariable=zipcode_text)
zipcode_entry.pack()

search_button = Button(app, text="Search Weather", width=12, command=search)
search_button.pack()

location_label = Label(app, text="Please enter a Zipcode", font=("bold", 20))
location_label.pack()

temp_label = Label(app, text="")
temp_label.pack()

temp_min_label = Label(app, text="")
temp_min_label.pack()

temp_max_label = Label(app, text="")
temp_max_label.pack()

weather_label = Label(app, text="")
weather_label.pack()

button_quit = Button(app, text="Quit", width=8, command=app.destroy)
button_quit.pack()



app.mainloop()

# zipcode = input("Enter Zipcode (USA): ")

# Request which allows us you fetch the weather information based on zipcode.
# Uses user input and converts units to imperial.
# weather_dat = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={user_input},us&units=imperial&appid={api_key}")

# if weather_data.json()['cod'] == '404':
#    print("Not A Proper Zipcode")
# else:
#
#
#
#
#
#    print()
#   print(f"The following is weather information for {location}, {user_input}:")
#    print()
#    print(f"Current forecast: {weather}")
#    print(f"Current temperature is: {temp}°F")
#   print(f"Minimum temperature of: {temp_min}°F")
#   print(f"Maximum temperature: {temp_max}°F")
