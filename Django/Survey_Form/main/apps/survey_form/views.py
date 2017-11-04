# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'survey_form/index.html')

def process(request):
	if 'attempt' not in request.session:
		request.session['attempt'] = 1
	else:
		request.session['attempt'] += 1
	if request.method == 'POST':
		request.session['name'] = request.POST['name']
		request.session['dojo_loc'] = request.POST['dojo_loc']
		request.session['languages'] = request.POST['languages']
		request.session['comment'] = request.POST['comment']
		return redirect('/result')
	else:
		return redirect('/')
def result(request):
	return render(request, 'survey_form/result.html')

def reset(request):
	request.session.flush()
	return redirect('/')

# Create your views here.
