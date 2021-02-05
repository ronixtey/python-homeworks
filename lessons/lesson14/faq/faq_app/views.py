from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

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

class RegisterView(generic.edit.FormView):
	form_class = UserCreationForm
	success_url = "users/login"
	template_name = "registration/register.html"

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

	def form_invalid(self, form):
		return super().form_invalid(form)


class CreateQuestion(generic.edit.CreateView):
	model = UserQuestion
	template_name = "faq/create_question.html"
	fields = ['title', 'body']
	# success_url = "/"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)		

	def get_success_url(self):
		return reverse("faq:index")

class UpdateQuestion(generic.edit.UpdateView):
	model = UserQuestion
	template_name = "faq/update_question.html"
	fields = ['title', 'body']

	def get_success_url(self):
		return reverse("faq:index")

class DeleteQuestion(generic.edit.DeleteView):
	model = UserQuestion
	template_name = "faq/question_confirm_delete.html"

	def get_success_url(self):
		return reverse("faq:index")
		