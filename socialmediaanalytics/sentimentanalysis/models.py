from django.db import models
#from django.contrib import admin
# Create your models here.
class Epidemic(models.Model):
	'''疫情类'''
	# 根据表建立属性
	cityEnglishName = models.TextField()
	cityName = models.TextField()
	#currentConfirmedCount = models.IntegerField()
	confirmedCount = models.IntegerField()
	curedCount = models.IntegerField()
	currentConfirmedCount = models.IntegerField()
	deadCount = models.IntegerField()
	locationId = models.IntegerField()
	suspectedCount = models.IntegerField()
	updateTime = models.CharField(max_length = 20)
'''
class Textmic(models,Model):
	"""docstring for Textmic"""
	textName=models.TextField()
	'''
#admin.site.register(Epidemic)
class China(models.Model):
	provinceName = models.TextField()
	confirmedCount = models.IntegerField()