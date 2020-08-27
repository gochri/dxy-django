# dxy-django

基于django的疫情数据&微博数据可视化

## Installation

```
$ git clone https://github.com/gochri/dxy-django
$ sudo pip3 install -r requirements.txt
$ cd socialmediaanalytics
```

##  Run

```
$ python manage.py runserver
```

* 疫情数据列表&分页展示 http://localhost:8000/sentimentanalysis/DXYAnalytics/
* 疫情数据可视化 http://localhost:8000/sentimentanalysis/D3Analytics/
* 微博数据列表 http://localhost:8000/weiboAnalytics/weiboList/
* 微博词云图 http://localhost:8000/weiboAnalytics/weiboPic/
* Kmeans聚类下的微博词云图 http://localhost:8000/weiboAnalytics/weiboKmeans/
* 管理员 http://localhost:8000/admin/login/?next=/admin/ admin/gochri

