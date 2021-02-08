from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView

from .models import *
from .forms import *

# Create your views here.
class IndexView(TemplateView):
	template_name = "fs/index.html"


class RegisterView(generic.edit.FormView):
	form_class = RegistrationForm
	success_url = "/login"
	template_name = "registration/register.html"

	def form_valid(self, form):
		#TODO
		# сделать автологин
		
		form.save()
		return super().form_valid(form)

	def form_invalid(self, form):
		return super().form_invalid(form)


class CategoriesView(generic.ListView):
	template_name = "fs/categories.html"
	context_object_name = "categories"

	def get_queryset(self):
		return Category.objects.all()


class SubcategoriesView(generic.DetailView):
	model = Category	
	template_name = "fs/subcategories.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)		
		context["subcategories"] = Subcategory.objects.filter(category=self.object.pk)
		return context


class ProductsView(generic.ListView):
	template_name = "fs/products.html"
	context_object_name = "products"

	def get_queryset(self):
		return Product.objects.all()


class ProductDetailView(generic.DetailView):
	model = Product


class CreateProductView(generic.edit.CreateView):
	model = Product
	template_name = "fs/new_product.html"
	fields = ['subcategory', 'name', 'description', 'price']

	# def get_context_data(self, **kwargs):
	# 	context = super(CreateProductView, self).get_context_data(**kwargs)
	# 	context['subcategory'] = Subcategory.objects.all()
	# 	return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse("fs:index") #products

class UpdateProductView(generic.edit.UpdateView):
	model = Product
	template_name = "fs/update_product.html"
	fields = ['subcategory', 'name', 'description', 'price']

	def get_success_url(self):
		return reverse("fs:index")	#products

class DeleteProductView(generic.edit.DeleteView):
	model = Product
	template_name = "fs/delete_product.html"

	def get_success_url(self):
		return reverse("fs:index") #products



class IndexRecieveLetterView(generic.ListView):
	model = Letter
	context_object_name = "letters"
	template_name = "fs/received_letters.html"
	
	def get_queryset(self):
		return Letter.objects.filter(receiver=self.request.user)

class IndexSenderLetterView(generic.ListView):
	model = Letter
	context_object_name = "letters"
	template_name = "fs/sent_letters.html"
	
	def get_queryset(self):
		return Letter.objects.filter(sender=self.request.user)

class DetailLetterView(generic.DetailView):
	model = Letter



class CreateLetterView(generic.edit.CreateView):
	model = Letter
	template_name = "fs/new_letter.html"
	fields = ['receiver', 'body']
	
	def form_valid(self, form):
		form.instance.sender = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse("fs:index") #sent letters

class UpdateLetterView(generic.edit.UpdateView):
	model = Letter
	template_name = "fs/update_letter.html"
	fields = ['receiver', 'body']

	def get_success_url(self):
		return reverse("fs:index")	

class DeleteLetterView(generic.edit.DeleteView):
	model = Letter
	template_name = "fs/delete_letter.html"

	def get_success_url(self):
		return reverse("fs:index") 