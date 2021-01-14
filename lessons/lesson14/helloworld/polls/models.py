import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	body = models.CharField(max_length=200)
	pub_date = models.DateTimeField('publishing date')

	def __str__(self):
		return self.body

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)	# ???

	

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	body = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.body



# после каждого изменения запускать - manage.py makemigrations polls