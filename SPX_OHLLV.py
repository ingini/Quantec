import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
from dateutil.relativedelta import relativedelta
import lxml
import re
import copy
import pymysql


def date_calculation():
	hello = datetime.datetime.now()
	nowdate = hello.strftime('%Y-%m-%d')

def SPX_CRAWLING():
	
	#크롬창 옵션
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument("--headless")
	options.add_argument("--no-sandbox")
	options.add_argument("--disable-dev-shm-usage")
	# LINUX 경로
	paths = '/home/tqtcore/quantec/QUANTQ1/src/QA/PYTHON/yahoo_news_crawling/chromedriver'
	driver = webdriver.Chrome(r'/home/tqtcore/quantec/QUANTQ1/src/QA/PYTHON/yahoo_news_crawling/chromedriver', options=options)	
	# CRAWLING
	driver.get('https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC')
	time.sleep(7)

	driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[1]/div[1]/div/div/div/span').click()

	time.sleep(3)
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[1]/div[1]/div/div/div/div/div/ul[2]/li[3]/button/span').click()
	time.sleep(3)
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[1]/button/span').click()
	time.sleep(3)

	driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()
	
	time.sleep(10)
	driver.close()
	# DOWNLOAD 받은 DATA
	df = pd.read_csv(r'^GSPC.csv', encoding='utf-8')
	df['ADJ_RATIO'] = df['Close'] / df['Adj Close']
	df =  df.sort_values(by=['Date'],axis=0, ascending=False)
	df.reset_index(inplace=True)
	df.drop(columns={'index'},inplace=True)
	df['Date'] = df['Date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
	df.to_csv(r'SPX_HISTORY.csv', encoding='utf-8',index=False)
	# preprocessing
	df2 = pd.read_csv(r'SPX_HISTORY.csv', encoding='utf-8')
	# 가장 최근의 값 load
	daily = df2.loc[[0]]
	daily['BASE_PRICE'] = df['Close'][1]
	daily['ADJ_1M'] = df['Close'][23]
	daily['ADJ_3M'] = df['Close'][63]
	daily['ADJ_6M'] = df['Close'][127]
	daily['ADJ_1Y'] = df['Close'][255]
	daily['ADJ_2Y'] = df['Close'][505]
	daily['CODE'] = '^GSPC'
	test = daily['Date'][0]
	daily.drop(columns={'Date'}, inplace=True)
	daily['Date'] = re.sub('-','',test)
	daily = daily[['Date','CODE','BASE_PRICE','Open','High','Low','Close','ADJ_1M','ADJ_3M','ADJ_6M','ADJ_1Y','ADJ_2Y']]

	# db 연결
	conn = pymysql.connect(host='localhost', port=51000, user='', password='', db='QTDB', charset='utf8')
	curs = conn.cursor()
	# db insert 하기전 각각의 값
	d_date = daily['Date'][0]
	d_code = daily['CODE'][0]
	d_open = daily['Open'][0]
	d_low = daily['Low'][0]
	d_close = daily['Close'][0]
	d_adj1m = daily['ADJ_1M'][0]
	d_adj3m = daily['ADJ_3M'][0]
	d_adj6m = daily['ADJ_6M'][0]
	d_adj1y = daily['ADJ_1Y'][0]
	d_adj2y = daily['ADJ_2Y'][0]
	d_base = daily['BASE_PRICE'][0]
	d_high = daily['High'][0]

	# db insert
	curs.execute("""INSERT INTO TC1011HS (`TRADE_DATE`,`CODE`,`BASE_PRICE`,`OPEN_PRICE`,`HIGH_PRICE`,`LOW_PRICE`, `LAST_PRICE`,`LAST_PRICE_1M`,`LAST_PRICE_3M`,`LAST_PRICE_6M`,`LAST_PRICE_1Y`,`LAST_PRICE_2Y`) VALUES(TRIM('%s'),TRIM('%s'), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE BASE_PRICE=%s, OPEN_PRICE=%s,HIGH_PRICE=%s,LOW_PRICE=%s,LAST_PRICE=%s,LAST_PRICE_1M=%s,LAST_PRICE_3M=%s,LAST_PRICE_6M=%s,LAST_PRICE_1Y=%s,LAST_PRICE_2Y=%s"""%(d_date,d_code,d_base,d_open,d_high,d_low,d_close,d_adj1m,d_adj3m,d_adj6m,d_adj1y,d_adj2y,d_base,d_open,d_high,d_low,d_close,d_adj1m,d_adj3m,d_adj6m,d_adj1y,d_adj2y))
	
	conn.commit()
	conn.close()

if __name__ == "__main__":
	SPX_CRAWLING()
