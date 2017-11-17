from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]*$')

# Create your models here.
class UsersManager(models.Manager):
	def validate(self, data):
		errors = []
		if len(data["first_name"]) < 2:
			errors.append("First name has to have more than 2 characters")
		if len(data["last_name"]) < 2:
			errors.append("Last name has to have more than 2 characters")
		if not LETTERS_ONLY.match(data["last_name"]) or not LETTERS_ONLY.match(data["first_name"]):
			errors.append("First and last name must be letters only")
		if not EMAIL_REGEX.match(data["email"]):
			errors.append("Invalid email entry")
		if len(data["password"]) < 8:
			errors.append("Please enter your password")
		if len(data['confirm_pw']) < 1:
			errors.append("Please confirm your password")
		if data["confirm_pw"] != data["password"]:
			errors.append("Confirm password does not match")
		if not errors:
			hash_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt().encode())
			user = users.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=hash_pw)
			return user
		else:
			return errors
		# errors = []
		# if len(data["first_name"]) < 2:
		# 	errors.append("First name has to have more than 2 characters")
		# if len(data["last_name"]) < 2:
		# 	errors.append("Last name has to have more than 2 characters")
		# if not LETTERS_ONLY.match(data["last_name"]) or not LETTERS_ONLY.match(data["first_name"]):
		# 	errors.append("First and last name must be letters only")
		# if not EMAIL_REGEX.match(data["email"]):
		# 	errors.append("Invalid email entry")
		# if len(data["password"]) < 8:
		# 	errors.append("Please enter your password")
		# if len(data['confirm_pw']) < 1:
		# 	errors.append("Please confirm your password")
		# if data["confirm_pw"] != data["password"]:
		# 	errors.append("Confirm password does not match")
		# if len(errors) == 0:
		# 	return True,
		# else:
		# 	return False, errors

	def validate_login(self, data):
		errors = []
		if not EMAIL_REGEX.match(data["email"]):
			errors.append("Invalid email entry")
		if len(data["password"]) < 8:
			errors.append("Please enter your password")
		if len(errors) == 0:
			return True,
		else:
			return False, errors

class users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UsersManager()