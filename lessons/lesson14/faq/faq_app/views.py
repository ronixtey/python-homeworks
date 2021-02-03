from django.shortcuts import render
from django.views import generic

from .models import *

#from .models import *
# Create your views here.
class IndexView(generic.ListView):
	model = UserQuestion
	# сам создает template_name: userquestion_list?
	template_name = "faq/index.html"

	def get_query_set(self):
		return UserQuestion.objects.all().order_by('pub_date')

class DetailView(generic.DetailView):
	model = UserQuestion
	template_name = "faq/detail.html"

class CreateQuestion(generic.edit.CreateView):
	model = UserQuestion
	fields = ['title', 'body']


