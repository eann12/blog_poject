from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
	title = models.CharField(verbose_name="Title", max_length=200)
	author = models.CharField(verbose_name="Author", max_length=100)
	body = models.CharField(verbose_name="Content", max_length=8000)
	created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True, blank=True)
	modified_date = models.DateTimeField(verbose_name="Modified Date", auto_now=True, blank=True)

	# def __int__(self):
	# 	return "%d" % self.id

class Comment(models.Model):
	comment = models.CharField(verbose_name="Comment", max_length=500)
	commenter = models.CharField(verbose_name="Comment by", max_length=100)	
	created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True, blank=True)
	modified_date = models.DateTimeField(verbose_name="Modified Date", auto_now=True, blank=True)

	post = models.ForeignKey(Post,on_delete = models.CASCADE)
