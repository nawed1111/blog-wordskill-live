from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

def add_to_group(sender, instance, created, **kwargs):
	if created:
		group=Group.objects.get(name='standard')
		instance.groups.add(group)

post_save.connect(add_to_group,sender=User)