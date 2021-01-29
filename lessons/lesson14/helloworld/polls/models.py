import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	body = models.CharField(max_length=200)
	pub_date = models.DateTimeField('publishing date', default=timezone.now())

	def __str__(self):
		return self.body

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	was_published_recently.admin_order_field = "pub_date"		# возможность сортировки = <по какому полю>
	was_published_recently.boolean = True		# символы вместо "True/False"
	was_published_recently.short_description = "Published recently?"	# отображение в заголовке

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	body = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.body

class UserChoice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	voting_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return f"{self.question} => {self.user}"









# после каждого изменения (кроме методов) запускать: 
# 1) manage.py makemigrations polls
# 2) manage.py migrate