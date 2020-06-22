from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .forms import CreatePostForm
from .models import *
from wordskill.decorators import *

from django.contrib.auth.decorators import login_required

# Create your views here.
def homeView(request):
	context = {}
	return render(request,'posts/home.html',context)


def blogView(request):
	posts = Posts.objects.all().filter(post_published = True)
#	comments = Comments.objects.all()
	context = {'posts':posts,}
	return render(request,'posts/blog.html',context)


@login_required(login_url='accounts:login')
@admin_only
def draftView(request):
	posts = Posts.objects.all().filter(post_published = False)
	context = {'posts':posts,}
	return render(request,'posts/post_drafts.html',context)

def postView(request,pk):
	post = Posts.objects.get(id=pk)
	comments = Comments.objects.all().filter(post=post, comment_posted = True)
	context = {'post':post,'comments':comments}
	return render(request,'posts/post.html',context)
	


@login_required(login_url='accounts:login')
@admin_only
def createPostView(request):
	form = CreatePostForm()
	posts = Posts.objects.all().filter(post_published = False)
	context = {'form':form,'posts':posts,}

	if request.method == 'POST':
		form = CreatePostForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render(request,'posts/post_drafts.html',context)
 
	return render(request,'posts/new_post_form.html',context)



@login_required(login_url='accounts:login')
@admin_only
def updatePostView(request,pk):
	post = Posts.objects.get(id=pk)
	form = CreatePostForm(instance=post)
	comments = Comments.objects.all().filter(post=post, comment_posted = False)
	context = {'form':form,'post':post,'comments':comments}
	if request.method == 'POST':
		form = CreatePostForm(request.POST,request.FILES,instance=post)
		if form.is_valid():
			form.save()
			return render(request,'posts/post.html',context)

	return render(request,'posts/new_post_form.html',context)


@login_required(login_url='accounts:login')
@admin_only
def deletePostView(request,pk):
	post = Posts.objects.get(id=pk)

	if request.method == 'POST':
		post.delete()
		return redirect('/')

	context = {'post':post,}
	return render(request,'posts/post_delete.html',context)


@login_required(login_url='accounts:login')
@admin_only
def publishPostView(request,pk):
	post = Posts.objects.get(id=pk)
	posts = Posts.objects.all().filter(post_published = True)
	context = {'posts':posts,'post':post,}
	if request.method == 'POST':
		post.post_published = True
		post.published_on = timezone.now()
		post.save()
		return render(request,'posts/blog.html',context)

	context = {'post':post,}
	return render(request,'posts/post_publish.html',context)


@login_required(login_url='accounts:login')
@admin_only
def publishToDraftView(request,pk):

	post = Posts.objects.get(id=pk)
	posts = Posts.objects.all().filter(post_published = True)
	context = {'posts':posts,'post':post,}

	post.post_published = False
	post.save()
	return render(request,'posts/blog.html',context)


@login_required(login_url='accounts:login')
def createCommentView(request,pk):

	if request.method == 'POST':
		data = request.POST
		post = Posts.objects.get(id=pk)
		model = Comments(post=post,username="savage",desc=data['comment_text'])
		model.save()

		comments = Comments.objects.all().filter(post=post, comment_posted = True)
		context = {'post':post,'comments':comments}
		return render(request,'posts/post.html',context)


@login_required(login_url='accounts:login')
@admin_only
def reviewCommentsView(request):
	comments = Comments.objects.all().filter(comment_posted = False)
	context = {'comments':comments,}
	return render(request,'posts/comments_review.html',context)


@login_required(login_url='accounts:login')
@admin_only
def deleteCommentView(request,pk):
	comment = Comments.objects.get(id=pk)

	comments = Comments.objects.all().filter(comment_posted = False)
	context = {'comment':comment,'comments':comments,}

	if request.method == 'POST':
		comment.delete()
		return render(request,'posts/comments_review.html',context)

	return render(request,'posts/comment_delete.html',context)


@login_required(login_url='accounts:login')
@admin_only
def publishCommentView(request,pk):
	comment = Comments.objects.get(id=pk)
	comments = Comments.objects.all().filter(comment_posted = False)
	context = {'comment':comment,'comments':comments,}

	if request.method == 'POST':
		comment.comment_posted = True
		comment.save()
		return render(request,'posts/comments_review.html',context)
		
	return render(request,'posts/comment_publish.html',context)