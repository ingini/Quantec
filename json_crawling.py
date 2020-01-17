import json
import requests
from urllib.request import urlopen
import pandas as pd
import datetime
import time


start_time = time.time()
#dataset = pd.read_excel('경로',encoding='utf-8')
# print(dataset.columns)
#uni = dataset['col'].unique()

page = "https://msxml.tenfore.com/IndexTS/?Username=id&password=pw&instrument=126.1.AIQ&sdate=01-01-1980&edate=14-01-2020&type=dailybar&JSONShort"
gg = urlopen(page)
response = requests.get(page).json()
contents = gg.read()
df2 = json.loads(contents)
# 파이썬 자료형 -> json 문자열
text = json.dumps(df2)
# json -> dict
json_val = json.dumps(df2)
df3 = json.dumps(df2, indent=4)
#print(df3)
test_df = pd.DataFrame.from_dict(df2, orient='index')

#test_df = test_df.T
print(test_df)
raw_data = json.loads(contents)

#print(raw_data)

'''print(raw_data.values())
#print(type(raw_data))
for i, e in enumerate(raw_data['results']):
    print(i, e['results'][0]['D953'])

api_list = [x for x in raw_data['results'][0]['data']]

print(api_list)'''

y_df = test_df['results'][0]
y_df = pd.DataFrame(y_df)
print(y_df)

data = y_df['data'][0]
data = pd.DataFrame(data)
print(data)
#print(data.info())

data['D953'] = pd.to_datetime(data['D953'])
print(data)



    # 크롤링한 종목 interpreter
    # print(x)
    # 총 프린트한 종목 갯수
    # print(x.count())
    # 받아온 데이터(x)의 저장
    # data.to_csv('저장할 경로%x.csv',encoding='euc-kr')


test1 = data['D953'].unique()
print(len(test1))
# 총 걸린 시간
print("waiting... {0:0.2f} Minutes".format((time.time() - start_time)/60))