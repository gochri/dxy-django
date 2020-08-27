#coding:utf-8
#在自己脚本中使用django model
import sys,os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'socialmediaanalytics.settings'  # 配置系统变量
import django
django.setup()

import csv
import requests
import json
import pandas as pd
#from sentimentanalysis.models import Epidemic
from sentimentanalysis.models import China

r=requests.get("https://lab.isaaclin.cn/nCoV/api/area?latest=1")
r.encoding='utf-8'
text=r.text
state=json.loads(text).get('results')
list=[]
for i in state:
	if i['countryName']=='中国':
		list.append(i)
china=[]
for k in list: 
	china.append({'provinceName':k['provinceName'], 'confirmedCount' :k['confirmedCount']})
df=pd.DataFrame(china)
df.to_csv("china.csv",encoding='utf_8_sig')

data_path = './china.csv'
with open(data_path,encoding='utf-8') as f:
   reader = csv.reader(f)
   for i, row in enumerate(reader):
      if i>0:
         china = China()
         china.provinceName = row[1]
         if row[2] != '':
            china.confirmedCount = int(row[2])
         else:
            china.confirmedCount = 0     
         china.save()
