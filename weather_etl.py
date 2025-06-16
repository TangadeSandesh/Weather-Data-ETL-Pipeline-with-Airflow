import requests
import pandas as pd
from pandas import json_normalize
import os
import s3fs

url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=2a3b5e655782807464772a5e2c2aac81"

headers = {
    "Accept" :"application/json",
    "Content-Type" : "application/json" 
}

def run_openweather_etl():
    response = requests.request("GET",url, headers=headers, data={})
    myData = response.json()

    df = pd.json_normalize(myData)

    csv_file_path = "s3://open-weather-data-bucket/weather_data.csv"

    # Check if the file already exists
    file_exists = os.path.isfile(csv_file_path)
    # print(file_exists)

    #Append without header if file exists
    df.to_csv(csv_file_path, mode='a', header=not file_exists, index=False, encoding="utf-8")
    # print("data saved in csv")