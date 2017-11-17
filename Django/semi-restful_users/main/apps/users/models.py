from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
	def validate(self, post_data):
		errors = []
		for dic, value in post_data.iteritems():
			if len(value) < 1:
				errors[dic] = "{} was not entered".format(dic)

		if not "email" in errors and not EMAIL_REGEX.match(post_data["email"]):
			errors['email'] = "Invalid email"
		return errors


class users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)