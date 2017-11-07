# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
	return render(request, 'session_words/index.html')

def process(request):
	addword = {}
	for key, value in request.POST.iteritems():
		if key != "bigfonts" and key != "csrfmiddlewaretoken":
			addword[key] = value
		if key == "bigfonts":
			addword['large'] = "large"
		else:
			addword['bigfonts'] = ""
	addword['created_at'] = datetime.now().strftime('%H:%M %p %m-%d-%Y')
	try:
		request.session['word']
	except KeyError:
		request.session['word'] = []

	wordlist = request.session['word']
	wordlist.append(addword)
	request.session['word'] = wordlist

	print addword

	return redirect('/')

def reset(request):
	request.session.flush()
	return redirect('/')

# Create your views here.
