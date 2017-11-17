from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
	return render(request, 'loginreg/index.html')

def register(request):
	result = users.objects.validate(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/')
	request.session['user_id'] = result.id
	messages.error(request, "Successfully registered")
	return redirect('/success')
	# if result[0]:
	# 	hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt().encode())
	# 	user = users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash_pw)
	# 	messages.error(request, "Successfully registered")
	# 	request.session['user_id'] = users.objects.get(id=user.id)
	# 	return redirect('/success')
	# else:
	# 	errors = result[1]
	# 	for error in errors:
	# 		messages.error(request, error)
	# 	return redirect('/')

def login(request):
	result = users.objects.validate_login(request.POST)
	if result[0]:
		user = users.objects.filter(email=request.POST['email'])
		if len(user) > 0:
			user = user[0]
			if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
				request.session['user_id'] = user.id
				messages.error(request, "Successfully log in")
				return redirect('/success')
			else:
				messages.error(request, "Password does not match")
				return redirect ('/')
	else:
		errors = result[1]
		for error in errors:
			messages.error(request, error)
		return redirect ('/')

def success(request):
	context = {
		"user": users.objects.get(id=request.session['user_id'])
	}
	return render(request, 'loginreg/success.html', context)