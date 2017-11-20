from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]\w+$')

# Create your models here.
class UserManager(models.Manager):
	def validate_reg(self, data):
		errors =[]
		if len(data['name']) < 1:
			errors.append("Please enter your name")
		if not LETTERS_ONLY.match(data['name']):
			errors.append("Name must be letters only")
		if len(data['alias']) < 1:
			errors.append("Please enter your alias")
		if len(data['email']) < 1:
			errors.append("Please enter your email")
		if len(self.filter(email=data['email'])) > 0:
			errors.append("Email already in use")
		if not EMAIL_REGEX.match(data['email']):
			errors.append("Invalid email entry")
		if len(data['password']) < 8:
			errors.append("please enter your password")
		if len(data['confirm_pw']) < 1:
			errors.append("Please confirm your password")
		if data['confirm_pw'] != data['password']:
			errors.append("Confirm password does not match")
		if not errors:
			hash_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt().encode())
			user = self.create(names=data['name'], alias=data['alias'], email=data['email'], password=hash_pw)
			return user
		else:
			return errors

	def validate_login(self, data):
		errors = []
		if len(self.filter(email=data['email'])) > 0:
			user = self.filter(email=data['email'])[0]
			if not bcrypt.checkpw(data['password'].encode(), user.password.encode()):
				errors.append("Incorrect password")
		else:
			errors.append("Incorrect email")

		if errors:
			return errors
		return user

class ReviewManager(models.Manager):
	def validate_rev(self, data):
		errors = []
		if len(data['title']) < 1 or len(data['review']) < 1:
			errors.append("Please enter something in the field")
		if not "author" in data and len(data['new_author']) < 1:
			errors.append("Please enter new author")
		if "author" in data and len(data['new_author']) > 0 and len(data['new_author']) < 3:
			errors.append("new author name must be 3 or more characters")
		if not int(data['ratings']) > 0 or not int(data['ratings']) <= 5:
			erros.append("invalid rating, please select a rating")
		return errors

	def add_review(self, data, user_id):
		this_author = None
		if len(data['new_author']) < 1:
			this_author = author.objects.get(id=int(data['author']))
		else:
			this_author = author.objects.create(name=data['new_author'])

		this_book = None
		if not book.objects.filter(title=data['title']):
			this_book = book.objects.create(title=data['title'], author=this_author)
		else:
			this_book = book.objects.get(title=data['title'])
		return self.create(
			review = data['review'],
			rate = data['ratings'],
			book = this_book,
			reviewer = user.objects.get(id=user_id)
			)

class user(models.Model):
	names = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	def __str__(self):
		return self.names

class author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(author, related_name="books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title

class Review(models.Model):
	review = models.TextField()
	rate = models.IntegerField()
	book = models.ForeignKey(book, related_name="reviews")
	reviewer = models.ForeignKey(user, related_name="user_reviews")
	created_at = models.DateTimeField(auto_now_add=True)
	objects = ReviewManager()
	def __str__(self):
		return "Book: {}".format(self.book.title)