from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def register(request):
	result = users.objects.validate_reg(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/')
	else:
		request.session['user_id'] = result.id
		messages.error(request, "You have successfully register")
		return redirect('/success')

def login(request):
	result = users.objects.validate_login(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/')
	else:
		request.session['user_id'] = result.id
		return redirect('/reviews/reviews')

def success(request):
	context = {
		"user": users.objects.get(id=request.session['user_id'])
	}
	return render(request, 'login/success.html', context)

def logout(request):
	request.session.flush()
	return redirect('/')