from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=200, null =True)

	def __str__(self):
		return self.name

class Posts(models.Model):
	
	title = models.CharField(max_length=200)
	description = RichTextField(blank=True, null=True)
	author = models.CharField(max_length=200)
	category = models.CharField(default = "Point of View", max_length=200)
	created_on = models.DateTimeField(auto_now_add= True)
	published_on =models.DateTimeField(blank = True, null = True)
	image = models.ImageField(blank = True, null=True)
	post_published = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag,blank=True)

	def __str__(self):
		return self.title

class Comments(models.Model):
	post = models.ForeignKey(Posts,null=True, on_delete=models.CASCADE, blank = True)
	username = models.CharField(default="savage", max_length=200)
	desc = models.CharField(max_length=1000)
	commented_on = models.DateTimeField(auto_now_add=True)
	comment_posted = models.BooleanField(default=False)




