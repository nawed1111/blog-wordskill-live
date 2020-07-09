from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .forms import CreatePostForm
from .models import *
from wordskill.decorators import *
from .filters import PostFilter
from django.contrib.auth.decorators import login_required
import calendar, datetime
# Create your views here.
def homeView(request):
	
	first_post = Post.objects.none()
	second_post = Post.objects.none()
	third_post = Post.objects.none()
	posts = Post.objects.none()

	posts = Post.objects.all().filter(post_published = True).order_by('-published_on')

	if posts.count() > 2 :
		first_post = posts.first()
		second_post = posts[1]
		third_post = posts[2]
	elif posts.count() == 2:
		first_post = posts.first()
		second_post = posts[1]
	elif posts.count() == 1:
		first_post = posts.first()

	posts = posts[3:7]

	current_year = timezone.now().strftime('%Y')
	current_month = timezone.now().strftime('%m')

	years = []
	months = []

	for month in range(1,int(current_month)+1):
		months.append(calendar.month_name[month])

	for year in range(2020,int(current_year)+1):
		years.append(year)

	context = {'posts':posts,'first_post':first_post,'second_post':second_post,'third_post':third_post,
				'current_year':current_year,'months':months,'years':years}

	return render(request,'posts/home.html',context)


def blogView(request):

	posts = Post.objects.all().filter(post_published = True).order_by('-published_on')
	post_filter = PostFilter(request.GET,queryset=posts)
	posts = post_filter.qs

	context = {'posts':posts,'post_filter':post_filter}
	return render(request,'posts/blog.html',context)


def filteredBlogViewOnCategory(request, category):

	posts = Post.objects.all().filter(post_published = True).filter(category__name = category).order_by('-published_on')
	post_filter = PostFilter(request.GET,queryset=posts)
	posts = post_filter.qs

	context = {'posts':posts,'post_filter':post_filter}
	return render(request,'posts/blog.html',context)

def filteredBlogViewOnMonth(request,month):

	datetime_object = datetime.datetime.strptime(month, "%B")
	month_number = datetime_object.month

	current_year = timezone.now().strftime('%Y')

	posts = Post.objects.all().filter(post_published = True).filter(published_on__month = month_number, published_on__year= current_year).order_by('-published_on')
	post_filter = PostFilter(request.GET,queryset=posts)
	posts = post_filter.qs

	context = {'posts':posts,'post_filter':post_filter,}
	return render(request,'posts/blog.html',context)

def filteredBlogViewOnYear(request,year):

	posts = Post.objects.all().filter(post_published = True).filter(published_on__year= year).order_by('-published_on')
	post_filter = PostFilter(request.GET,queryset=posts)
	posts = post_filter.qs

	context = {'posts':posts,'post_filter':post_filter,}
	return render(request,'posts/blog.html',context)


@login_required(login_url='accounts:login')
@admin_only
def draftView(request):
	posts = Post.objects.all().filter(post_published = False).order_by('-created_on')
	posts_count = posts.count()
	context = {'posts':posts,'posts_count':posts_count}
	return render(request,'posts/post_drafts.html',context)

def postView(request,pk):
	post = Post.objects.get(id=pk)
	
	context = {'post':post}
	return render(request,'posts/post.html',context)


@login_required(login_url='accounts:login')
@admin_only
def createPostView(request):
	form = CreatePostForm()
	posts = Post.objects.all().filter(post_published = False)
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
	post = Post.objects.get(id=pk)
	form = CreatePostForm(instance=post)
	posts = Post.objects.all().filter(post_published = False)

	context = {'form':form,'post':post,'posts':posts}
	if request.method == 'POST':
		form = CreatePostForm(request.POST,request.FILES,instance=post)
		if form.is_valid():
			form.save()
			return render(request,'posts/post_drafts.html',context)

	return render(request,'posts/new_post_form.html',context)


@login_required(login_url='accounts:login')
@admin_only
def deletePostView(request,pk):
	post = Post.objects.get(id=pk)

	if request.method == 'POST':
		post.delete()
		return redirect('/')

	context = {'post':post,}
	return render(request,'posts/post_delete.html',context)


@login_required(login_url='accounts:login')
@admin_only
def publishPostView(request,pk):
	post = Post.objects.get(id=pk)
	context = {'post':post,}
	if request.method == 'POST':
		post.post_published = True
		post.published_on = timezone.now()
		post.save()
		return render(request,'posts/post.html',context)

	context = {'post':post,}
	return render(request,'posts/post_publish.html',context)


@login_required(login_url='accounts:login')
@admin_only
def publishToDraftView(request,pk):

	post = Post.objects.get(id=pk)
	post.post_published = False
	post.save()

	posts = Post.objects.all().filter(post_published = False).order_by('-created_on')
	posts_count = posts.count()

	context = {'posts':posts,'post':post,'posts_count':posts_count}

	
	return render(request,'posts/post_drafts.html',context)
