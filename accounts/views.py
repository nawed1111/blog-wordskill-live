from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import *

from wordskill.decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def registerView(request):
	form=CreateUserForm()

	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,"Account created successfully for "+user)
			return redirect('accounts:login')

	current_year = timezone.now().strftime('%Y')
	context = {'form':form, 'current_year':current_year}
	return render(request,'accounts/register.html',context)


@unauthenticated_user
def loginView(request):

	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('posts:home')
		else:
			messages.info(request,"Username or Password incorrect!")
			return render(request,'accounts/login.html')

	current_year = timezone.now().strftime('%Y')

	context = {'current_year':current_year}
	return render(request,'accounts/login.html',context)

def logoutView(request):
	logout(request)
	return redirect('posts:home')

def userProfileView(request):

	context = {}
	return render(request,'accounts/user.html',context)