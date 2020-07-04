from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse
# Create your models here.

# class Profile(models.Model):
# 	user = models.OneToOneField(User,on_delete=models.CASCADE)
# 	name = models.CharField(max_length=200)
# 	email = models.CharField(max_length=200)
# 	date_created = models.DateTimeField(auto_now_add=True)
	
# 	def __str__(self):
# 		return self.name	


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('accounts:user')