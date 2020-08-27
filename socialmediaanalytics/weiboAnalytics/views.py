from django.shortcuts import render
from weiboAnalytics.models import Weibo

import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import pickle
import jieba
import xlrd

import numpy as np
from sklearn.cluster import KMeans

import re
from sklearn import metrics
from sklearn import preprocessing

# Create your views here.

def weiboKmeans(request):
	weibo_list = Weibo.objects.all()
	zero=np.zeros((len(weibo_list),3))
	j=0
	for i in weibo_list:
		words = i.words
		zhong = re.compile('钟南山')
		health = re.compile('健康')
		day = re.compile('每天')
		zhong_find = re.findall(zhong, words)
		zero[j][0]=len(zhong_find)
		health_find = re.findall(health, words)
		zero[j][1]=len(health_find)
		day_find = re.findall(day, words)
		zero[j][0]=len(day_find)
		#if(i.like<5):
		#	zero[j][0]+=1
		j+=1
	print(zero)

	estimator = KMeans(n_clusters=2)
	estimator.fit(zero)
	label_pred = estimator.labels_
	print(label_pred)
	#print(zero.shape)
	#print(type(zero))
	#zero_scaled = preprocessing.scale(zero)
	#print(zero_scaled)
	print(metrics.silhouette_score(zero, label_pred, metric='euclidean'))

	z=0
	f = open("KMeans0.txt",'a')
	for i in weibo_list:
		if label_pred[z]==0:
			words = i.words
			f.write(words)
		z+=1
	text = ''

	data_path = './KMeans0.txt'
	with open(data_path,'r',encoding='gbk') as fin:
		for line in fin.readlines():
			line = line.strip('\n')
			text += ' '.join(jieba.cut(line))
			text += ' '
			fout = open('KMeans0text.txt','wb')
			pickle.dump(text,fout)
			fout.close()
	fr=open('KMeans0text.txt','rb')
	text=pickle.load(fr)
	print("加载成功")
	backgroud_Image=plt.imread('./china.jpg')
	print('加载图片成功！')

	wc=WordCloud(
		background_color='white',
		mask=backgroud_Image,
		font_path='C:\Windows\Fonts\STZHONGS.TTF', #若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
		max_words=2000,
		stopwords=STOPWORDS,
		max_font_size=150,
		random_state=30
		)
	wc.generate_from_text(text)
	print('开始加载文本')
	img_colors=ImageColorGenerator(backgroud_Image)
	wc.recolor(color_func=img_colors)
	plt.imshow(wc)
	plt.axis('off')
	plt.savefig("./static/images/KMeans0.png")

	z=0
	f = open("KMeans1.txt",'a')
	for i in weibo_list:
		if label_pred[z]==1:
			words = i.words
			f.write(words)
		z+=1
	text = ''

	data_path = './KMeans1.txt'
	with open(data_path,'r',encoding='gbk') as fin:
		for line in fin.readlines():
			line = line.strip('\n')
			text += ' '.join(jieba.cut(line))
			text += ' '
			fout = open('KMeans1text.txt','wb')
			pickle.dump(text,fout)
			fout.close()
	fr=open('KMeans1text.txt','rb')
	text=pickle.load(fr)
	print("加载成功")
	backgroud_Image=plt.imread('./china.jpg')
	print('加载图片成功！')

	wc=WordCloud(
		background_color='white',
		mask=backgroud_Image,
		font_path='C:\Windows\Fonts\STZHONGS.TTF', #若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
		max_words=2000,
		stopwords=STOPWORDS,
		max_font_size=150,
		random_state=30
		)
	wc.generate_from_text(text)
	print('开始加载文本')
	img_colors=ImageColorGenerator(backgroud_Image)
	wc.recolor(color_func=img_colors)
	plt.imshow(wc)
	plt.axis('off')
	plt.savefig("./static/images/KMeans1.png")

	context={
		'weibo_list':weibo_list,
		#'plt':plt,
		}
	return render(request, 'weiboKmeans.html', context)


def weiboPic(request):
	weibo_list = Weibo.objects.all()
	print(len(weibo_list))
	f = open("chinanews.txt",'a')
	for i in weibo_list:
		if i!=100:
			print(100)
		#rows_value = table.row_values(i)
		words = i.words
		f.write(words)
	text = ''
	#数据集路径
	data_path = './chinanews.txt'
	with open(data_path,'r',encoding='gbk') as fin:
		for line in fin.readlines():
			line = line.strip('\n')
			text += ' '.join(jieba.cut(line))
			text += ' '
			fout = open('text.txt','wb')
			pickle.dump(text,fout)
			fout.close()
	fr=open('text.txt','rb')
	text=pickle.load(fr)
	print("加载成功")
	backgroud_Image=plt.imread('./china.jpg')
	print('加载图片成功！')
	wc=WordCloud(
		background_color='white',
		mask=backgroud_Image,
		font_path='C:\Windows\Fonts\STZHONGS.TTF', #若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
		max_words=2000,
		stopwords=STOPWORDS,
		max_font_size=150,
		random_state=30
		)
	wc.generate_from_text(text)
	print('开始加载文本')
	img_colors=ImageColorGenerator(backgroud_Image)
	wc.recolor(color_func=img_colors)
	plt.imshow(wc)
	plt.axis('off')
	plt.savefig("./static/images/chinanews.png")	
	context={
		'weibo_list':weibo_list,
		#'plt':plt,
		}
	return render(request, 'weiboPic.html', context)

def weiboAnalytics(request):
	weibo_list = Weibo.objects.all()
	context={
		'weibo_list':weibo_list,
		}
	return render(request, 'weiboAnalytics.html', context)


