from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def validate(self, post_data):
		errors = []
		if len(post_data['name']) < 1:
			errors.append("Please enter name")
		if len(post_data['desc']) < 1:
			errors.append("please enter description")
		if len(errors) == 0:
			return True,
		else:
			return False, errors

class courses(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CourseManager()
