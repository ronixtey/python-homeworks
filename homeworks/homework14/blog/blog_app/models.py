from django.db import models
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=144, default=" ")
	body = models.CharField(max_length=1024)
	pub_date = models.DateTimeField(default=timezone.now());
	user = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	body = models.CharField(max_length=144)
	pub_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.body