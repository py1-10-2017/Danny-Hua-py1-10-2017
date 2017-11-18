from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]\w+$')

# Create your models here.
class UsersManager(models.Manager):
	def validate_reg(self, data):
		errors = []
		if len(data['name']) < 1:
			errors.append("Please enter your name")
		if not LETTERS_ONLY.match(data['name']):
			errors.append("Name must be letters only")
		if len(data['alias']) < 1:
			errors.append("Please enter your alias")
		if len(data['email']) < 1:
			errors.append("Please enter your email")
		if len(users.objects.filter(email=data['email'])) > 0:
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
			user = users.objects.create(name=data['name'], alias=data['alias'], email=data['email'], password=hash_pw)
			return user
		else:
			return errors

	def validate_login(self, data):
		errors = []
		if len(users.objects.filter(email=data['email'])) > 0:
			user = users.objects.filter(email=data['email'])[0]
			if not bcrypt.checkpw(data['password'].encode(), user.password.encode()):
				errors.append("Incorrect password")
		else:
			errors.append("Incorrect email")

		if errors:
			return errors
		return user

class users(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UsersManager()