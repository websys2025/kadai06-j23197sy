import requests
import pandas as pd

#気象庁APIで天気予報データ
#対応する各地点のコードから天気を読み込む
#今回は千葉県(120000)の地域コード

API_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json" #エンドポイント
response = requests.get(API_URL)
data = response.json()

time_series = data[0]['timeSeries']
for series in time_series:
    if 'weatherCodes' in series['areas'][0]:
        time_defines = series['timeDefines']
        weather_areas = series['areas']
        break

records = []
for area in weather_areas:
    obs_name = area['area']['name']
    for i, date in enumerate(time_defines):
        records.append({
            '観測所': obs_name,                           #観測所
            '日付': date,                                 #日付
            '天気コード': area['weatherCodes'][i],        #天気
            '天気説明': area['weathers'][i]               #天気説明
        })

df = pd.DataFrame(records)
print(df)
