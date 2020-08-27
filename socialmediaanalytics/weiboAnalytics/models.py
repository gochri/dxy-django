from django.db import models

# Create your models here.
class  Weibo(models.Model):
	"""docstring for  Weibomic
	def __init__(self, arg):
		super( Weibomic, self).__init__()
		self.arg = arg
		"""
	address = models.TextField()
	words = models.TextField()
	#keyword = models.TextField()
	#frequency = models.IntegerField()
	time = models.TextField()
	like = models.IntegerField()
	name = models.TextField()
	source = models.TextField()