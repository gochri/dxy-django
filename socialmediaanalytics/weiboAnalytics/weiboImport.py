#在自己脚本中使用django model
import sys,os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'socialmediaanalytics.settings'  # 配置系统变量
import django
django.setup()


from weiboAnalytics.models import Weibo

import xlrd

#weibo_path = './微博数据.xls'
workbook = xlrd.open_workbook('./微博数据.xls')
#print (workbook.sheet_names())
table = workbook.sheets()[0]
#print (table.nrows) #17
for i in range(1,table.nrows-1):
	weibo = Weibo()
	rows_value = table.row_values(i)
	weibo.address = rows_value[7]
	weibo.words = rows_value[4]
	#weibo.keyword = 'after'
	#weibo.frequency = 1
	weibo.time = rows_value[6]
	weibo.like = rows_value[11]
	weibo.name = rows_value[0]
	weibo.source = rows_value[8]
	weibo.save()