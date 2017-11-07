# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

items = [
	{'id': 1,
	'item': 'Dojo T-shirt',
	'price': 19.99},
	{'id': 2,
	'item': 'Dojo sweater',
	'price': 29.99},
	{'id': 3,
	'item': 'Dojo Cup',
	'price': 4.99},
	{'id': 4,
	'item': 'Algorithm Book',
	'price': 49.99}
	]

def index(request):
	if 'last_trans' in request.session.keys():
		del request.session['last_trans']

	context = {
		"items": items
	}
	return render(request, 'amadon/index.html', context)

def buy(request, item_id):
	quantity = int(request.POST['quantity'])
	for item in items:
		if item['id'] == int(item_id):
			amt_charged = item['price'] * quantity

	try:
		request.session['sum_charged']
	except KeyError:
		request.session['sum_charged'] = 0

	try:
		request.session['sum_items']
	except KeyError:
		request.session['sum_items'] = 0

	sum_charged = request.session['sum_charged']
	sum_charged += amt_charged
	request.session['sum_charged'] = sum_charged

	sum_items = request.session['sum_items']
	sum_items += quantity
	request.session['sum_items'] = sum_items

	request.session['last_trans'] = amt_charged
	return redirect('/amadon/checkout')

def checkout(request):
	return render(request, 'amadon/checkout.html')

def reset(request):
	request.session.flush()
	return redirect('/')
# Create your views here.
