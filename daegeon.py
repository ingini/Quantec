# -*- coding : utf-8 -*-
# daegeon.py

import os
import pandas as pd
import numpy as np
from selenium import webdriver
#from webdriver_manager import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import lxml
import copy

starttime = time.time()
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
path = "C:/Users/user/PycharmProjects/untitled5/news_analysis/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path, options=options)
name = pd.read_excel('미국주식.xlsx')
name_list = name['종목코드'][:1]
print(name_list.count())
link_list = []
for ticker in name_list:
    # yahoo 접속
    driver.get('https://finance.yahoo.com')
    time.sleep(18)

    search = driver.find_element_by_xpath('//*[@id="yfin-usr-qry"]')

    name_key = ticker

    search.send_keys(name_key)

    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="search-button"]').click()

    time.sleep(15)
    driver.execute_script("window.scrollTo(0,400)")

    # 뉴스 클릭

    driver.find_element_by_xpath('//*[@id="Col1-3-Summary-Proxy"]/section/div/div/a[1]/div/span').click()
    time.sleep(5)

    news_link = []
    for order in range(1, 11):
        try:
            news_link = driver.find_element_by_xpath(f'//*[@id="latestQuoteNewsStream-0-Stream"]/ul/li[{order}]/div/div/div[2]/h3/a').get_property('href')
            print('ok')
            time.sleep(1)
        except:
            pass

        link = [ticker, news_link]
        link_list.append(link)


link_frame = pd.DataFrame(link_list, columns=['ticker', 'news_link'])
#link_frame = link_frame['news_link'].apply(lambda x : x.drop_duplicates())
print(link_frame)


#link_frame = link_frame.groupby('ticker')['news_link'].apply(lambda x: x.drop_duplicates()).reset_index()

news_list = []
for link in link_frame['news_link']:
    if len(link) > 1:
        driver.get(link)
        print(link)
        time.sleep(11)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        title = soup.find('h1')
        titles = []
        for text in title:
            title = title.get_text()
            titles.append(title)
        date = soup.find('time')
        dates = []
        for text in date:
            date = date.get_text()
            dates.append(date)
        media = soup.find('a')
        medias = []
        for text in media:
            media = media.get_text()
            medias.append(media)
        texts = soup.find('p')
        body = []
        for text in texts:
            temp_text = texts.get_text()
            body.append(temp_text)

        temp_data = [link, titles, dates, medias, body]
        news_list.append(temp_data)
    else:
        print('error')

news_frame = pd.DataFrame(news_list, columns=['news_link', 'title', 'date', 'media','article'])
result_df = link_frame.merge(news_frame, on= 'news_link', how= left)

print(result_df)
print(time.time() - starttime)



#result_df = result_df.drop_duplicates('news_link').drop(['Unnamed: 0_x', 'Unnamed: 0_y'], axis =1).reset_index(drop='index')









