import pandas as pd
import numpy as np
import datetime
import os
import requests
import matplotlib.pyplot as plt
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
import time
import re
from urllib.request import urlopen
import copy
import sqlite3 as sq
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator, get_single_color_func
import random
import webbrowser
from collections import Counter
# from tabulate import tabulate
import threading
from PIL import Image
from selenium import webdriver
import pymysql
import zipfile
from sqlalchemy import create_engine
# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

engine = create_engine('mysql+pymysql://tqtdb:' + 'tqtdb1!' + '@14.39.135.217:50000/QTIDB', encoding='utf-8')
cons = engine.connect()
#conn = pymysql.connect(host='172.16.71.90', port=49990, user='tqtdb', password='tqtdb1!', db='hdgdb', charset='utf8')
#curs = conn.cursor()

def etf_aum():
    #path = os.getcwd() # 현재 디렉토리
    path = os.path.dirname(os.path.realpath(__file__)) #현재 파일 경로
    os.chdir(path)

    pd.set_option('expand_frame_repr', False)
    pd.reset_option('display.precision', 10)
    pd.set_option('max_colwidth', 10)
    pd.set_option('colheader_justify', 'left')
    option = Options()
    option.add_argument('--start-fullscreen')
    driver = webdriver.Chrome(r'C:/Users/quantec/Desktop/etf_finder/Chromedriver.exe', chrome_options=option)
    driver.implicitly_wait(60)

    driver.get('https://www.etf.com/etfanalytics/etf-finder')
    driver.execute_script("window.scrollTo(0, 300)")
    driver.find_element_by_xpath('//*[@id="top-login-btn"]/ul/li/a').click() # login

    email = 'kmkim@quantecinvest.co.kr'
    password = 'dhwlddj10'

    loginid = driver.find_element_by_xpath('//*[@id="edit-name"]')
    loginid.send_keys(email)
    loginpw = driver.find_element_by_xpath('//*[@id="edit-pass"]')
    loginpw.send_keys(password)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="user_login"]').click()
    driver.implicitly_wait(60)
    time.sleep(15)
    driver.execute_script("window.scrollTo(0, 1500)")
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="accordion__body-8"]/div[1]/label/input').click()
    driver.find_element_by_xpath('//*[@id="accordion__body-8"]/div[2]/label/input').click()
    driver.find_element_by_xpath('//*[@id="accordion__body-8"]/div[3]/label/input').click()
    driver.find_element_by_xpath('//*[@id="accordion__body-8"]/div[4]/label/input').click()
    driver.find_element_by_xpath('//*[@id="accordion__body-8"]/div[5]/label/input').click()
    driver.find_element_by_xpath('//*[@id="accordion__body-8"]/div[6]/label/input').click()
    driver.implicitly_wait(60)
    driver.find_element_by_xpath('//*[@id="table-tabs"]/li[7]').click()
    driver.implicitly_wait(60)
    driver.find_element_by_xpath('//*[@id="more-btn"]').click()
    driver.implicitly_wait(60)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[4]').click()
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[4]/span/label').click() #Issuer
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[5]/span/label').click() #Brand
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[6]/span/label').click() #Launch Date
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[7]/span/label').click() # Economic Development
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[12]/span/label').click() # Segments
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[13]/span/label').click() # Strategy
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[14]/span/label').click() #ETN
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[15]/span/label').click() # APS
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[16]/span/label').click() # Underlying index
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[19]/span/label').click() # inverse
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[20]/span/label').click() # leveraged
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[21]/span/label').click() #leveraged factor
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[27]/span/label').click() # expencse ratio
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[28]/span/label').click() # AUM
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[31]/span/label').click() # spread %
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[32]/span/label').click() #spread
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[39]/span/label').click()# grade
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[40]/span/label').click()# effi
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[41]/span/label').click()# trada
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[42]/span/label').click()# fit
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[2]/div[44]/span/label').click() # fundclosure risk
    driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div/section/div[3]/button[2]').click()
    driver.execute_script("window.scrollTo(0, 1800)")
    driver.find_element_by_xpath("//*[@value='100']").click()
    driver.execute_script("window.scrollTo(0, 7000)")



    df = []


    def extract(df):
        result = bs(driver.page_source, 'lxml')
        result = result.find_all('table', id='finderTable')[0].find_all('tr')

        for i in range(1,len(result)):
            df.append([result[i].find_all('td')[0].text.replace(' ',''), result[i].find_all('td')[1].text, result[i].find_all('td')[2].text, result[i].find_all('td')[3].text, result[i].find_all('td')[4].text, result[i].find_all('td')[5].text, result[i].find_all('td')[6].text, result[i].find_all('td')[7].text,                       result[i].find_all('td')[8].text,  result[i].find_all('td')[9].text,                       result[i].find_all('td')[10].text,  result[i].find_all('td')[11].text,                       result[i].find_all('td')[12].text,  result[i].find_all('td')[13].text, result[i].find_all('td')[14].text,  result[i].find_all('td')[15].text, result[i].find_all('td')[16].text,  result[i].find_all('td')[17].text,  result[i].find_all('td')[18].text,  result[i].find_all('td')[19].text,  result[i].find_all('td')[20].text,  result[i].find_all('td')[21].text, result[i].find_all('td')[22].text,  result[i].find_all('td')[23].text,  result[i].find_all('td')[24].text,  result[i].find_all('td')[25].text, result[i].find_all('td')[26].text,  result[i].find_all('td')[27].text])

        return df

    for i in range(23):
        driver.execute_script("window.scrollTo(0, 8500)")
        time.sleep(3)
        if i >= 1:
            driver.find_element_by_xpath('//*[@id="nextPage"]').click()
            time.sleep(1)
        df = extract(df)

    df = pd.DataFrame(df)
    df.columns = ['Ticker','Fund Name','Asset Class','Issuer','Brand','Launch Date', 'Economic Developement','Geography','Category','Focus','Niche','Segments','Strategy','ETN','Active Per Sec',\
        'Underlying Index','Inverse','Leveraged','Leveraged Factor','Expense Ratio', 'AUM','Spread%','spread','Grade','Efficiency','Tradabillity','Fit','Fund Closure Risk']



    #sql_query = 'SELECT * FROM CODE_MASTER_TEMP WHERE Global ID investment = "ETF"'
    #symbol = pd.read_sql_query(sql_query, conn)

    # convert 'Launch Date' to same format

    df['Launch Date'] = pd.to_datetime(df['Launch Date'])

    # saving 'AUM' to 'AUM_str'

    df['AUM_str'] = df['AUM']

    # define values

    million = 10 ** 6
    billion = 10 ** 9
    kilo = 10 ** 3

    # modifying string to values

    for i in range(0, len(df['AUM'])):
        if 'M' in df['AUM'].iloc[i]:
            df['AUM'].iloc[i] = float(df['AUM'].iloc[i].lstrip('$').rstrip('M')) * million
            print(df['AUM'].iloc[i])
        elif 'B' in df['AUM'].iloc[i]:
            df['AUM'].iloc[i] = float(df['AUM'].iloc[i].lstrip('$').rstrip('B')) * billion
            print(df['AUM'].iloc[i])
        elif 'K' in df['AUM'].iloc[i]:
            df['AUM'].iloc[i] = float(df['AUM'].iloc[i].lstrip('$').rstrip('K')) * kilo
            print(df['AUM'].iloc[i])
        elif '-' in df['AUM'].iloc[i]:
            df['AUM'].iloc[i] = float(0)
            print(df['AUM'].iloc[i])
        else:
            print(df['AUM'].iloc[i], 'ERROR')
            break

    '''    
    i = 0
    for i in range(len(df)):
        try:
            dfsymbol = str(df['AUM'][i])
            sql = "INSERT INTO CODE_MASTER_HDG (Symbol, Company_name, SNP_YN) VALUES (%s, %s, %s) "
            data = (str(dfsymbol))
            curs.execute(sql, data)
        finally:
            pass

    conn.commit()
    conn.close()

    '''
    writer = pd.ExcelWriter('etf.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=True)
    writer.save()
    writer.close()
    df.to_sql(name='etf_finder', con=engine, if_exists='append', index=False)
    conn.commit()
    conn.close()


etf_aum()