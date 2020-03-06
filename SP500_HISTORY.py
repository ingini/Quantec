import pandas as pd
import numpy as np
from dateutil.parser import parse
import datetime as dt
import time


df = pd.read_excel(r'S&P_500_historical_holdings.xlsx', encoding='utf-8')


Ticker = df.Ticker
Corp_name = df.Name


df.drop(columns={'Name','Detail Holding Type'}, inplace=True)


#Ticker = Ticker.tolist()

df2 = df.T
df2.reset_index(inplace=True)



df2.rename(columns={'index':'ASOFDATE'},inplace=True)


'''
with open(r's&p_history.csv', 'a') as f:
    df2.to_csv(f, encoding='utf-8', index=False, header=None)
    f.close()
'''

df = pd.read_csv(r's&p_history.csv', encoding='utf-8')

df.rename(columns={'Ticker':'ASOFDATE'},inplace=True)




df['ASOFDATE'] = pd.to_datetime(df['ASOFDATE'])
df['ASOFDATE'].dt.strftime('%Y-%m-%d')
#pd.to_datetime(df['ASOFDATE'], format='%Y-%m-%d %H:%M:S').dt.strftime('%Y-%m-%d')

print("##################################")
print(df)
print(Ticker)

##test##
#Ticker = df.columns.tolist()


i=0

for ticker in Ticker:
    try:
        sym = pd.DataFrame()
        sym['ASOFDATE'] = df['ASOFDATE']
        sym['SYMBOL'] = ticker
        sym[i] = df[ticker]
        sym.rename(columns={i:'value'},inplace=True)
        sym.to_csv(r'./s&p_history/'+ticker+'.csv', encoding='utf-8', index=False)
        #sym"%d" %d=i
        #sym.ticker = ticker
        #sym.reset_index(inplace=True)
        i += 1
    except:
        continue

time.sleep(30)

ticker_m = pd.read_csv(r'./s&p_history/AAPL.csv', encoding='utf-8')
for ticker in Ticker:
    try:
        ticker_j = pd.read_csv(r'./s&p_history/'+ticker+'.csv', encoding='utf-8')
        print(ticker_j)
        ticker_m = ticker_m.append(ticker_j)
    except:
        print('error')
        continue

print(ticker_m)

ticker_m.to_csv(r'./s&p_history/s&p_history.csv', encoding='utf-8', index=False, header=None)