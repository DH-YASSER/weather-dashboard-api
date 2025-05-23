# Real-time weather fetcher using Open-Meteo (no API key needed)
import urllib.request
import json

def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(city)}&count=1"
    with urllib.request.urlopen(url) as res:
        data = json.loads(res.read().decode())
    if not data.get("results"):
        raise ValueError(f"City '{city}' not found.")
    r = data["results"][0]
    return r["latitude"], r["longitude"], r["name"], r["country"]

def get_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,is_day"
        f"&timezone=auto"
    )
    with urllib.request.urlopen(url) as res:
        return json.loads(res.read().decode())

import urllib.parse

def main():
    city = input("Enter city name: ") or "London"
    lat, lon, name, country = get_coordinates(city)
    data = get_weather(lat, lon)
    c = data["current"]
    print(f"\nWeather in {name}, {country}:")
    print(f"  Temperature : {c['temperature_2m']}°C")
    print(f"  Humidity    : {c['relative_humidity_2m']}%")
    print(f"  Wind Speed  : {c['wind_speed_10m']} km/h")
    print(f"  Time of Day : {'Day' if c['is_day'] else 'Night'}")

if __name__ == "__main__":
    main()
