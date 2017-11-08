# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

lists = [
	{"place": "Farm",
	"earns": "(earn 10-20 golds)"},
	{"place": "Cave",
	"earns": "(earn 5-10 golds)"},
	{"place": "House",
	"earns": "(earn 2-5 golds)"},
	{"place": "Casino",
	"earns": "(earn/takes 0-50 golds)"}
	]

def index(request):
	if "gold" not in request.session:
		request.session['gold'] = 0
	if 'activities' not in request.session:
		request.session['activities'] = []
		
	context = {
		"lists": lists
	}
	return render(request, "ninjagold/index.html", context)

def process(request):
	date = datetime.now().strftime('%A, %d. %B %Y %I:%M %p')
	place = request.POST['place']
	if place == "Farm":
		money = random.randint(10, 20)
		color = "win"
	elif place == "Cave":
		money = random.randint(5, 10)
		color = "win"
	elif place == "House":
		money = random.randint(2, 5)
		color = "win"
	else:
		money = random.randint(-50, 50)
		if money < 0:
			color = "loss"
		else:
			color = "win"
	request.session['activities'].append({'act': "{} {} gold from the {}! ".format(color, money, place), 'color': color, 'time':date})
	request.session['gold'] += money

	return redirect('/')

def reset(request):
	request.session.flush()
	return redirect('/')

# Create your views here.
