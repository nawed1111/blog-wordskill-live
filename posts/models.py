from django.db import models
from ckeditor.fields import RichTextField


from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=200, null =True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200, null =True)

	def __str__(self):
		return self.name

class Post(models.Model):
	
	title = models.CharField(max_length=200)
	description = RichTextField(blank=True, null=True)
	author = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add= True)
	published_on =models.DateTimeField(blank = True, null = True)
	image = models.ImageField(blank = True, null=True)
	post_published = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag,blank=True)
	comments = GenericRelation(Comment)
	
	def __str__(self):
		return self.title








