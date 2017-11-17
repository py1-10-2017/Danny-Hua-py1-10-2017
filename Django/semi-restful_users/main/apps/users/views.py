from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.messages import error

def index(request):
	if request.method == 'POST':
		print request.POST
		users.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
		return redirect('/users')
	else:
		context = {
			"users": users.objects.all()
		}
		return render(request, 'users/index.html', context)

def new(request):
	return render(request, 'users/new.html')

def show(request, user_id):
	errors = users.objects.validate(request.POST)
	if len(errors):
		for dic, message in errors.iteritems():
			error(request, message, extra_tags=dic)
			return redirect('users/new')

	elif request.method == 'POST':
		user = users.objects.get(id=user_id)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
		return redirect('/users')
	else:
		context = {
			"user": users.objects.get(id=user_id)
		}
	return render(request, 'users/show.html', context)

def edit(request, user_id):
	context = {
			"user": users.objects.get(id=user_id)
		}
	return render(request, 'users/edit.html', context)

def destroy(request, user_id):
	users.objects.get(id=user_id).delete()
	return redirect('/users')


# Create your views here.
