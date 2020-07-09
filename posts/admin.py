from django.contrib import admin
from .models import Post, Tag, Category
# from import_export import resources, fields
# from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)


# class PostResource(resources.ModelResource):
# 	category = fields.Field(column_name='category',attribute='category',widget=ForeignKeyWidget(Category, 'name'))

# 	tags = fields.Field(column_name='tags',attribute='tags',widget=ManyToManyWidget(Tag, field='name'))  

# 	class Meta:
# 		  model = Post
# 		  skip_unchanged = True
# 		  report_skipped = True
# 		  exclude = ('id', )
# 		  import_id_fields = ('name',)
# 		  fields = ('name', 'title', 'description', 'author', 'category', 'published_on', 'image', 'post_published','tags', 'comments')