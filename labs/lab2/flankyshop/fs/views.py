from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.base import TemplateView

from .models import *

# Create your views here.
class IndexView(TemplateView):
	template_name = "fs/index.html"

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


# class ProductsView(generic.DetailView):
# 	model = Subcategory
# 	template_name = "fs/products"

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)		
# 		context["products"] = Products.objects.filter(subcategory=self.object.pk)
# 		return context


