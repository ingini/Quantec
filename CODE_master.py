import numpy as np
import pandas as pd
import math
import zipfile
import pymysql
import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import time
from sqlalchemy import create_engine
# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

conn = pymysql.connect(host='172.16.71.90', port=49990, user='tqtdb', password='tqtdb1!', db='hdgdb', charset='utf8')
curs = conn.cursor()
'''
############################ 날짜  -filezila update 맞춰서 배치 돌릴려면 2일 잡아야 오류없이 잘 돌아감!
today = datetime.datetime.today()
month = today - relativedelta(months=1)
today = today - datetime.timedelta(days=2)
today = today.strftime("%Y-%m-%d")
month = month.strftime("%Y-%m")
print(month)
print(today)
'''
'''
zf_us = zipfile.ZipFile('Daily_SecurityReference_'+today+'.zip')
df2 = pd.read_csv(zf_us.open("Daily_SecurityReference_"+today+".dat"), sep='|', header=None)

cods = df2[(df2[2]==1001)]
cods.drop(columns={2},inplace=True)
cods.reset_index(inplace=True)

i= 0
for i in range(len(cods)):
    try:
        dfcompanyid = str(cods[0][i])
        dfshareid = str(cods[1][i])
        dfsymbol = str(cods[3][i])
        sql = "INSERT INTO CODE_M (Corp_code, shareclassid, Symbol) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE Corp_code=%s,shareclassid = %s, Symbol=%s"
        data = (str(dfcompanyid), str(dfshareid) ,str(dfsymbol),str(dfcompanyid),str(dfshareid),str(dfsymbol))
        curs.execute(sql, data)

    finally:
        pass
'''

month = '2020-1'
# CODE_M

Delta_Financial = zipfile.ZipFile('C:/Users/quantec/Desktop/Monthly_SecurityReference_'+month+'.zip')
df = pd.read_csv(Delta_Financial.open('Monthly_SecurityReference_'+month+'.dat'), sep='|',header=None)
print(df)

cod = df[(df[2]==1001)]
cod.drop(columns={2},inplace=True)
cod.reset_index(inplace=True)

i= 0
for i in range(len(cod)):
    try:
        dfcode = str(cod[0][i])
        dfnames = str(cod[1][i])
        dfsymbol = str(cod[3][i])
        sql = "INSERT INTO CODE_M (Corp_code, shareclassid, Symbol) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE Corp_code=%s,shareclassid = %s, Symbol=%s"
        data = (str(dfcode), str(dfnames),str(dfsymbol),str(dfcode),str(dfnames),str(dfsymbol))
        curs.execute(sql, data)
    finally:
        pass


conn.commit()
conn.close()

# CODE_MASTERs
'''
coded = df[[2,3]]
#coded.rename(columns={0:'corp',1:"names",2:'Corp_name',3:'symbols'},inplace=True)
#print(code['code'][666])
#print(df2[13][19441:][:5])

i=0
for i in range(len(coded)):
    try:
        dfcode = str(coded['corp'][i])
        dfnames = str(coded['Corp_name'][i])
        dfsymbol = str(coded['symbols'][i])
        sql = "INSERT INTO CODE_MASTERS (Corp_code, full_name, Symbols) VALUES (%s, %s, %s) "
        data = (str(dfcode), str(dfnames), str(dfsymbol))
        curs.execute(sql, data)
    finally:
        pass

conn.commit()
conn.close()
'''

import pandas as pd
import numpy as np
import math
import zipfile
import os

import pathlib
import pymysql
import datetime
from sqlalchemy import create_engine
# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

conn = pymysql.connect(host='', port=, user='', password='', db='db명', charset='utf8')
curs = conn.cursor()
engine = create_engine('mysql+pymysql://loginID:' + 'PW' + '@IP:PORT/DB명', encoding='utf-8')
cons = engine.connect()





'''

#################D _ valuation#####################
szsql = "SELECT shareclassid FROM CODE_M "
curs.execute(szsql)
conn.commit()
codename = [item[0] for item in curs.fetchall()]

ds = pd.DataFrame()
cod = pd.DataFrame()
dfs = pd.DataFrame()
zf_us = zipfile.ZipFile('Daily_ValuationRatios_2020-01-06.zip')

col = [14000,14003,14004,14005,14021]

for i in range(len(codename)):
    print("현재몇개째? : ",i, "총 완성해야되는 갯수 : ",len(codename))
    try:
        df2 = pd.read_csv(zf_us.open("Daily_ValuationRatios_"+codename[i]+"_2020-01-06.dat"), sep='|', header=None)
        df = df2[(df2[1]==14000)]
        ds = ds.append(df)
        df = df2[(df2[1]==14003)]
        ds = ds.append(df)
        df = df2[(df2[1]==14004)]
        ds = ds.append(df)
        df = df2[(df2[1]==14005)]
        ds = ds.append(df)
        df = df2[(df2[1] == 14021)]
        ds = ds.append(df)
        dfs = ds.pivot(0, 1, 2)
        dfs.reset_index(inplace=True)
        dfs['date'] = '2020-01-06'
        dfs.to_csv('Daily2_valuationratios2020-01-06.csv', encoding='utf-8')
    except:
        continue


#dfs.to_csv('Daily2_valuationratios2020-01-06.csv', encoding='utf-8')
print('##############################')



#ds.to_sql(name='D_valuationsm', con=engine, if_exists='append', index=False)

''''''
#################D _ Financial#####################
szsql = "SELECT Corp_code FROM CODE_M "
curs.execute(szsql)
conn.commit()
Corp_code = [item[0] for item in curs.fetchall()]
szsql2 = "SELECT shareclassid FROM CODE_M "
curs.execute(szsql2)
conn.commit()
shareclassid = [item[0] for item in curs.fetchall()]
szsql3 = "SELECT A.Corp_code FROM ( SELECT Corp_code FROM CODE_M UNION SELECT shareclassid FROM CODE_M ) A"
curs.execute(szsql3)
conn.commit()
codename = [item[0] for item in curs.fetchall()]

df_Corp = pd.DataFrame()
df_Share = pd.DataFrame()
ds_Corp = pd.DataFrame()
ds_Share = pd.DataFrame()

zf_us = zipfile.ZipFile('Delta_FinancialStatementsAOR_2020-02-03.zip')

code_exist = pathlib.Path("Delta_FinancialStatementsAOR_"+codename[i]+"_2020-02-03.dat")
file_exist = pathlib.Path("Delta_FinancialStatementsAOR_"+Corp_code[i]+"_2020-02-03.dat")
files_exist = pathlib.Path("Delta_FinancialStatementsAOR_"+shareclassid[i]+"_2020-02-03.dat")


col = [26185, 20046, 23374, 23220,23044,23030,23028,23029,23001,23212,23213,23214,23108,23331,23226,23351,23008,23312,23275,23319,23282,23301,23340,23098,23097,23411,23412,23413,23541,23063,23339,23528,23047,23143,23000,23103,23151,23260,23353,23497,23379,23384,23027,23232,20392,23204,23132,20100,20108,20046,20045,20018,20007,20151,20109,20190,20189,20057,20177,20136,20091,20093,20346,26010,26060,26053,26298,26229,26230,26231,26232,26179,26274,26009,26008,26229,26063,26027,26015,26016]

for i in range(len(codename)):
    print("현재몇개째? : ",i, "총 완성해야되는 갯수 : ",len(codename))
    if i == 3000:
        break
    print(codename[i] in Corp_code)
    try:
        df2 = pd.read_csv(zf_us.open("Delta_FinancialStatementsAOR_" + codename[i] + "_2020-02-03.dat"), sep='|', header=None)
        print("open")
        if codename[i] in Corp_code:
            print("Corp open")
            co=0
            for co in range(len(col)):
                print(col[co])
                cod = df2[(df2[1] == col[co])]
                cod.reset_index(inplace=True)
                ds_Corp = ds_Corp.append(cod)
                df_Corp = ds_Corp.pivot(0, 1, 2)
                df_Corp['date'] = '2020-02-03'
                print("ok")
        elif codename[i] in shareclassid :
                for ca in range(len(col)):
                    cods = df2[(df2[1] == col[ca])]
                    cods.reset_index(inplace=True)
                    ds_Share = ds_Share.append(cods)
                    df_Share = ds_Share.pivot(0, 1, 2)
                    df_Corp['date'] = '2020-02-03'
                    print("share!")
        else:
            print(codename[i], "는 codename에는 있지만 corp_code와 shareclassid에는 없습니다.")
        df_Corp.to_csv('Delta3_FinancialStatementsAOR_Corp_code_2020-02-03.csv', encoding='utf-8', index=False)
        df_Share.to_csv('Delta3_FinancialStatementsAOR_Corp_code_2020-02-03.csv', encoding='utf-8', index=False)
    except:
        continue


        elif os.path.isfile("경로"):
            try:
                for j in range(len(Corp_code)):
                    df2 = pd.read_csv(zf_us.open("Delta_FinancialStatementsAOR_"+Corp_code[j]+"_2020-02-03.dat"), sep='|', header=None)
                    for c in range(len(col)):
                        cod = df[(df[1] == col[c])]
                        cod.reset_index(inplace=True)
                        ds_Corp = ds_Corp.append(cod)
                        df_Corp = ds_Corp.pivot(0, 1, 2)
                        df_Corp['date'] = '2020-02-03'
                        #df_Corp.to_csv('Delta2_FinancialStatementsAOR_Corp_code_2020-02-03.csv', encoding='utf-8')
            except:
                continue
        elif files_exist.exists():
            try:
                for y in range(len(shareclassid)):
                    df3 = pd.read_csv(zf_us.open("Delta_FinancialStatementsAOR_"+shareclassid[y]+"_2020-02-03.dat"), sep='|', header=None)
                    for c in range(len(col)):
                        cod = df[(df[1] == col[c])]
                        cod.reset_index(inplace=True)
                        ds_Share = ds_Share.append(cod)
                        df_Share = ds_Share.pivot(0, 1, 2)
                        df_Share['date'] = '2020-02-03'
                        #df_Share.to_csv('Delta2_FinancialStatementsAOR_shareclassid_2020-02-03.csv', encoding='utf-8')
                except:
                    continue
        else:
            continue
    else:
        continue
'''



#df_Corp.to_csv('Delta2_FinancialStatementsAOR_Corp_code_2020-02-03.csv', encoding='utf-8')
#df_Share.to_csv('Delta2_FinancialStatementsAOR_shareclassid_2020-02-03.csv', encoding='utf-8')


#dfs.to_csv('Delta2_FinancialStatementsAOR2020-02-03.csv', encoding='utf-8')
#dfs.to_csv('Delta_FinancialStatementsAOR2020-02-03.csv', encoding='utf-8')
