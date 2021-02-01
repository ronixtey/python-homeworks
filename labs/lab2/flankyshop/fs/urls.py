from django.urls import path

from . import views

app_name = "fs"	
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.SubcategoriesView.as_view(), name='subcategories'),
#    path('categories/products', views.SubcategoriesView.as_view(), name='products')
]