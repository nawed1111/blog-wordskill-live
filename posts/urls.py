from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
	path('',views.homeView,name = 'home'),
	path('blog/',views.blogView,name = 'blog'),
	path('drafts/',views.draftView,name = 'drafts'),
	path('post/<str:pk>/',views.postView,name = 'post'),
	path('new_post/',views.createPostView,name = 'new_post'),
	path('edit_post/<str:pk>/',views.updatePostView,name = 'edit_post'),
	path('delete_post/<str:pk>/',views.deletePostView,name = 'delete_post'),
	path('publish_post/<str:pk>/',views.publishPostView,name = 'publish_post'),
	path('send_to_draft_post/<str:pk>/',views.publishToDraftView,name = 'send_to_draft_post'),
    path('comment/<str:pk>/',views.createCommentView,name = 'comment'),
    path('review_comments/',views.reviewCommentsView,name = 'review_comments'),
    path('delete_comment/<str:pk>/',views.deleteCommentView,name = 'delete_comment'),
    path('publish_comment/<str:pk>/',views.publishCommentView,name = 'publish_comment'),
]