from django.db import models
from django.utils import timezone


class Post(models.Model):
	body = models.CharField(max_length=144)
	pub_date = models.DateTimeField(default=timezone.now());

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	body = models.CharField(max_length=144)
	pub_date = models.DateTimeField(default=timezone.now())

