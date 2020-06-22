from django.forms import ModelForm
from .models import Posts
from django import forms


class CreatePostForm(ModelForm):
    class Meta:
        model=Posts
        fields='__all__'
        exclude = ('published_on','post_published')
