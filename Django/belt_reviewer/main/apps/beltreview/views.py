from django.shortcuts import render, HttpResponse, redirect

from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request, 'beltreview/index.html')

def register(request):
	result = user.objects.validate_reg(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/')
	else:
		print result.id
		request.session['user_id'] = result.id
		messages.error(request, "You have successfully register")
		return redirect('/success')

def login(request):
	result = user.objects.validate_login(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/')
	else:
		request.session['user_id'] = result.id
		return redirect('/reviews')

def success(request):
	context = {
		"user": user.objects.get(id=request.session['user_id'])
	}
	return render(request, 'beltreview/success.html', context)

def logout(request):
	request.session.flush()
	return redirect('/')

def review(request):
	recent_review = Review.objects.all().order_by('-created_at')[:3]
	more_review = Review.objects.all().order_by('-created_at')[3:]
	context = {
		"recent": recent_review,
		"more": more_review,
		"user": user.objects.get(id=request.session['user_id'])
	}
	return render(request, 'beltreview/reviews.html', context)

def add_book_review(request):
	context = {
		"authors": author.objects.all()
	}
	return render(request, 'beltreview/add.html', context)

def create(request):
	result = Review.objects.validate_rev(request.POST)
	if result:
		for error in result:
			messages.error(request, error)
	else:
		book_id = Review.objects.add_review(request.POST, request.session['user_id']).book.id
	return redirect('/book/{}'.format(book_id))

def show_book(request, book_id):
	context = {
		"book": book.objects.get(id=book_id)
	}
	return render(request, 'beltreview/showbook.html', context)

def create_add(request, book_id):
	this_book = book.objects.get(id=book_id)
	new_book_review = {
		'title': this_book.title,
		'author': this_book.author.id,
		'ratings': request.POST['ratings'],
		'review': request.POST['review'],
		'new_author': ''
	}
	result = Review.objects.validate_rev(new_book_review)
	if result:
		for error in result:
			messages.error(request, error)
	else:
		Review.objects.add_review(new_book_review, request.session['user_id'])
	return redirect('/book/{}'.format(book_id))

def other_user(request, user_id):
	total_reviews = len(Review.objects.filter(reviewer_id=user_id))
	context = {
		'User': user.objects.get(id=user_id),
		'reviews': Review.objects.filter(reviewer_id=user_id),
		'tot_reviews': total_reviews
	}
	return render(request, 'beltreview/user.html', context)
