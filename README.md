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

  <p align="center"><img src="pictures/DXYAnalytics.png" width="480"\></p>

* 疫情数据可视化 http://localhost:8000/sentimentanalysis/D3Analytics/

  <p align="center"><img src="pictures/D3Analytics.png" width="480"\></p>

* 微博数据列表 http://localhost:8000/weiboAnalytics/weiboList/

  <p align="center"><img src="pictures/weiboList.png" width="480"\></p>

* 微博词云图 http://localhost:8000/weiboAnalytics/weiboPic/

  <p align="center"><img src="socialmediaanalytics/static/images/chinanews.png" width="480"\></p>

* Kmeans聚类下的微博词云图 http://localhost:8000/weiboAnalytics/weiboKmeans/

  <p align="left"><img src="socialmediaanalytics/static/images/KMeans0.png" width="240"\><img src="socialmediaanalytics/static/images/KMeans0.png" width="240"\></p>

* 管理员 http://localhost:8000/admin/login/?next=/admin/ admin/gochri

