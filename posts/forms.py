from django.forms import ModelForm
from .models import Post
from django import forms


class CreatePostForm(ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        exclude = ('published_on','post_published')
