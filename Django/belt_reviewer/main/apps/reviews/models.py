from __future__ import unicode_literals

from django.db import models
from ..login.models import users

class ReviewManager(models.Manager):
	def validate_review(self, data):
		errors = []

class author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(author, related_name="books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class review(models.Model):
	review = models.TextField()
	rating = models.IntegerField()
	book = models.ForeignKey(book, related_name="reviews")
	reviewer = models.ForeignKey(users, related_name="user_reviews")
	created_at = models.DateTimeField(auto_now_add=True)