import django_filers

from .models import *

class OrderPost(django_filers.FilerSet):
	class Meta:
		model = Posts
		fields = '__all__'