from django.db import models

# Create your models here.

class Post(models.Model):

	title = models.TextField(blank=False)
	author = models.TextField(blank=False)
	content = models.TextField(blank=False)
	date_posted = models.TimeField(blank=False)

