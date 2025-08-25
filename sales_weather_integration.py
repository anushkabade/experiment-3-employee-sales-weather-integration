

\f0\fs24 \cf0 import requests\
import pandas as pd\
\
sales_file = "sales_data.xlsx"\
sales_df = pd.read_excel(sales_file)\
\
print("Sales data loaded successfully")\
print(sales_df.head())\
\
API_KEY = "YOUR_API_KEY"\
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"\
\
def fetch_weather(city_name):\
    params = \{\
        "q": city_name,\
        "appid": API_KEY,\
        "units": "metric"\
    \}\
    try:\
        response = requests.get(BASE_URL, params=params)\
        data = response.json()\
        if response.status_code == 200:\
            return \{\
                "temperature": data["main"]["temp"],\
                "humidity": data["main"]["humidity"],\
                "weather": data["weather"][0]["description"]\
            \}\
        else:\
            return \{"temperature": None, "humidity": None, "weather": None\}\
    except:\
        return \{"temperature": None, "humidity": None, "weather": None\}\
\
weather_list = []\
for index, row in sales_df.iterrows():\
    city = row["city"]\
    weather_info = fetch_weather(city)\
    weather_list.append(weather_info)\
\
weather_df = pd.DataFrame(weather_list)\
combined_df = pd.concat([sales_df.reset_index(drop=True), weather_df], axis=1)\
\
output_file = "sales_with_weather.xlsx"\
combined_df.to_excel(output_file, index=False)\
\
print(f"Combined dataset saved as: \{output_file\}")\
print(combined_df.head())\
}
