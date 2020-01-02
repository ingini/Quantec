"""
	System	: QT System
	Author	: Quantec Inc.
	Module	: news search
	File	: get_news_url.py
"""

# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.getenv('_QA_SRC_PYTHON') + '/lib')
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import pymysql
import logging
import qtlog
import qtdblib

#실행 시
#main("TXN") 과 같이 미국 증시 코드를 string타입 파라미터로 입력하면 됨.

def get_key(code, conn):

	#테이블에서 code에 해당하는 키워드 검색
	curs = conn.cursor()

	szsql = "SELECT NAME_KOR, CODE \
			FROM TC9001CD \
			WHERE CODE = %s"
	
	curs.execute(szsql, (code))
	rows	= curs.fetchone()
	
	#return ['KEYWORD1', 'KEYWORD2']
	
	if rows == None:
		#return [code, code]
		return ['appl', 'apple']
	else :
		return [rows[0], rows[1]]
	'''
	return ['KEYWORD1', 'KEYWORD2']
	'''

def get_news(df, key, page, conn):
	[code, opt]=get_key(key, conn)
	#code, opt =get_key(key, conn)
	
	id = page-1
	link = 'https://search.naver.com/search.naver?&where=news&query='+code +'+'+ opt +'&start='+str(page)
	addr = requests.get(link)
	soup = BeautifulSoup(addr.content, 'html.parser')
	articles = soup.select("ul.type01 > li")
	now = datetime.datetime.now()

	for ar in articles:
		titles = ar.select_one('a._sp_each_title').text
		medias = ar.select_one('span._sp_each_source').text
		dates = ar.select_one('dd.txt_inline').text
		urls = ar.select_one('a._sp_each_title').get('href')
		titles = re.sub('\u200b','',titles)
		dat = re.findall('\d+',dates)
		dat = ''.join(dat)
		dat = int(dat)
		if '시간 전' in dates:
			result = now - datetime.timedelta(hours=dat)
			dat = result
			dat = dat.strftime('%Y%m%d')
		elif '달 전' in dates:
			result = now - datetime.timedelta(month=dat)
			dat = result
			dat = dat.strftime('%Y%m%d')
		elif '일 전' in dates:
			result = now - datetime.timedelta(days=dat)
			dat = result
			dat = dat.strftime('%Y%m%d')
		elif '분 전' in dates:
			result = now - datetime.timedelta(minutes=dat)
			dat = result
			dat = dat.strftime('%Y%m%d')
		elif '초 전' in dates:
			result = now - datetime.timedelta(seconds=dat)
			dat = reslut
			dat = dat.strftime('%Y%m%d')
		else:
			pass
			
		titles = re.sub('\u200b','',titles)
		df.loc[id] = [titles, urls, key, medias, dat]
		id+=1
	print(df)
	return df

'''
def export_result(df):
	engine = create_engine('mysql+mysqldb://tqtdb:tqtdb1!@192.168.0.93:50000/QTDB', encoding='utf-8') conn = engine.connect()
	#TB2 테이블에서 code 검색 #TB2 테이블은 TITLE과 LINK, CODE로 구성됨. TITLE은 기사 제목, LINK는 기사 URL, CODE는 미국 증시 코드가 저장됨.  df.to_sql(name='TB2', con=engine, if_exists='append', index=False)
	
	conn.close()
'''
def get_news_url_sub(code, conn):
	init_data = {'title' : [''], 'link': [''], 'code': [''],'media':[''],'date':['']}
	
	df = pd.DataFrame(init_data)
	
	idx = 0;
	#code = sys.argv[1]
	news_page = [1, 11, 21, 31]
	#news_page 는 현재 4페이지를 가져오도록 되어있음. 한 페이지에 10개의 기사가 표시됨. 추가로 가져와야하는 경우 41, 51 과 같이 추가 가능.
	for page in news_page:
		df = get_news(df, code, page, conn)

	df = df.rename(columns={'title':'TITLE', 'link':'LINK', 'code':'CODE'})
	i=0
	for i in range(len(df)):
		try:
			sz = str(df['TITLE'][i])
			print(sz)
		except:
			sz= [x.encode('utf-8','ignore') for x in sz]
			print(sz)
			pass

	#export_result(df)

def get_news_url(zprocnm, zbatchnm, zlognm):
	
	qtlog.SetLoginfo(zlognm)
	
	conn	= qtdblib.QTDBConnect()
	get_news_url_sub('AAPL', conn)
	
	conn.close()

get_news_url('qa_8200_mp', 'get_news_url', '/home/tqtcore/quantec/QUANTQ3/LOG/QA/20191229/qa_8200_mp')

#END OF FILE
