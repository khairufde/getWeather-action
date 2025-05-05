import pandas as pd
import requests
import json
import os


def get_weather_data():
    city_name = 'london'
    api_key = os.getenv('WEATHER_API_KEY')

    coor_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}'
    coor_req = requests.get(coor_url)
    coor_req.raise_for_status()
    coor_data = coor_req.json()

    if coor_data:
        lat = str(coor_data[0]['lat'])
        lon = str(coor_data[0]['lon'])
    else:
        print("No data found")
        return pd.DataFrame()

    fore_url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
    fore_req = requests.get(fore_url)
    json_data = json.loads(fore_req.text)

    forecast_list = json_data.get('list', [])
    weather_data = []

    for forecast in forecast_list:
        dt = pd.to_datetime(forecast['dt_txt'])
        weather = forecast['weather'][0]
        main = forecast['main']
        wind = forecast['wind']
        
        weather_data.append({
            'date': dt.date(),
            'time': dt.strftime('%H:%M:%S'),
            'weather': weather['main'],
            'weather_desc': weather['description'],
            'temp': main['temp'],
            'feels_like': main['feels_like'],
            'temp_min': main['temp_min'],
            'temp_max': main['temp_max'],
            'pressure': main['pressure'],
            'humidity': main['humidity'],
            'wind_speed': wind['speed'],
            'wind_deg': wind['deg'],
            'wind_gust': wind.get('gust', None)
        })

    weather_df = pd.DataFrame(weather_data)

    if not weather_df.empty:
        weather_df[['year', 'month', 'day']] = weather_df['date'].astype(str).str.split('-', expand=True)
        weather_df.drop(columns=['date'], inplace=True)
        cols = ['year', 'month', 'day'] + [col for col in weather_df.columns if col not in ['year', 'month', 'day']]
        weather_df = weather_df[cols]

    return weather_df


if __name__ == "__main__":
    weather_df = get_weather_data()
    if not weather_df.empty:
        weather_df.to_csv("weather_forecast.csv", index=False)
        print("CSV file saved as weather_forecast.csv")
    else:
        print("No data to save.")
