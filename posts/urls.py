from django.urls import path,include
from . import views

app_name = 'posts'

urlpatterns = [
	path('',views.homeView,name = 'home'),
	path('blog/',views.blogView,name = 'blog'),
	path('drafts/',views.draftView,name = 'drafts'),
	path('post/<str:pk>/',views.postView,name = 'post'),
	path('blog/<str:category>/',views.filteredBlogViewOnCategory,name = 'filter_post'),
	path('month/<str:month>/',views.filteredBlogViewOnMonth,name = 'months'),
	path('year/<int:year>/',views.filteredBlogViewOnYear,name = 'years'),
	path('new_post/',views.createPostView,name = 'new_post'),
	path('edit_post/<str:pk>/',views.updatePostView,name = 'edit_post'),
	path('delete_post/<str:pk>/',views.deletePostView,name = 'delete_post'),
	path('publish_post/<str:pk>/',views.publishPostView,name = 'publish_post'),
	path('send_to_draft_post/<str:pk>/',views.publishToDraftView,name = 'send_to_draft_post'),
]