# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# request.session['attempt'] = 0
def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	else:
		request.session['count'] += 1
	return render(request, 'randomword/index.html')

def generate(request):
	if request.method == 'POST':
		randomword = get_random_string(length=14)
		request.session['randomword'] = randomword
		return redirect('/')
	else:
		return redirect('/')

def reset(request):
	request.session.flush()
	return redirect('/')
# Create your views here.
