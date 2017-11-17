from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
	context = {
		"courses": courses.objects.all()
	}
	return render(request, 'courses/index.html', context)

def add(request):
	result = courses.objects.validate(request.POST)
	if result[0]:
		courses.objects.create(name=request.POST['name'], desc=request.POST['desc'])
	else:
		errors = result[1]
		for error in errors:
			messages.error(request, error)
	return redirect('/')

def show(request, course_id):
	context = {
		"course": courses.objects.get(id=course_id)
	}
	return render(request, 'courses/remove.html', context)

def delete(request, course_id):
	courses.objects.get(id=course_id).delete()
	return redirect('/')