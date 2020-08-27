#coding:utf-8
#在自己脚本中使用django model
import sys,os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'socialmediaanalytics.settings'  # 配置系统变量
import django
django.setup()

import csv

from sentimentanalysis.models import Epidemic
# 从csv读取数据并存入models创建的表里
data_path = './DXYArea-TimeSeries-china-hubei-xiangyan.csv'
with open(data_path,encoding='utf-8') as f:
   reader = csv.reader(f)
   for i, row in enumerate(reader):
      if i>0:
         epidemic = Epidemic()
         epidemic.cityEnglishName = row[1]
         #epidemic.confirmedCount = int(row[1])
         epidemic.cityName = row[2]
         #epidemic.suspectedCount = int(row[2])
         if row[3] != '':
            epidemic.confirmedCount = int(row[3])
         else:
            epidemic.confirmedCount = 0
         #epidemic.curedCount = int(row[3])
         if row[4] != '':
            epidemic.curedCount = int(row[4])
         else:
            epidemic.curedCount = 0
         #epidemic.deadCount = int(row[4])
         if row[5] != '':
            epidemic.currentConfirmedCount = int(row[5])
         else:
            epidemic.currentConfirmedCount = 0
         if row[6] != '':
            epidemic.deadCount = int(row[6])
         else:
            epidemic.deadCount = 0
         if row[7] != '':
            epidemic.locationId = int(row[7])
         else:
            epidemic.locationId = 0
         if row[8] != '':
            epidemic.suspectedCount = int(row[8])
         else:
            epidemic.suspectedCount = 0
         epidemic.updateTime = row[9]
         epidemic.save()