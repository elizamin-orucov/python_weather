from tkinter import *
from PIL import ImageTk, Image
import requests

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "913a9d018060805a15ab47e2bce323f0"
icon_url = "http://openweathermap.org/img/wn/{}@2x.png"


def getWeather(city):
    params = {
        "q": city,
        "appid": api_key,
    }
    data = requests.get(url, params=params).json()
    if data:
        try:
            city = data["name"].capitalize()
            country = data["sys"].get("country")
            temperature = int(data["main"].get("temp") - 273.15)
            icon = data["weather"][0].get("icon")
            condition = data["weather"][0].get("description")
            return (city, country, temperature, icon, condition)
        except:
            print("City not found. Make sure you spelled the city name correctly.")


def main():
    city = cityEntry.get()
    weather = getWeather(city)
    if weather:
        location_label["text"] = f"{weather[0]},{weather[1]}"
        tempLabel["text"] = f"{weather[2]}°C"
        conditionLabel["text"] = f"{weather[4]}"
        icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url.format(weather[3]), stream=True).raw))
        icon_label.configure(image=icon)
        icon_label.image = icon


app = Tk()
app.geometry("300x450")
app.title("hava")

cityEntry = Entry(app, justify="center")
cityEntry.pack(fill=BOTH, ipady=10, padx=18, pady=5)
cityEntry.focus()

search_button = Button(app, text="search", font=("Arial", 15), command=main)
search_button.pack(fill=BOTH, ipady=10, padx=20)

icon_label = Label(app)
icon_label.pack()

location_label = Label(app, font=("Arial", 40))
location_label.pack()

tempLabel = Label(app, font=("Arial", 50, "bold"))
tempLabel.pack()

conditionLabel = Label(app, font=("Arial", 20))
conditionLabel.pack()

app.mainloop()


