from django.urls import path

from . import views

app_name = "fs"	
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
	path('users/register', views.RegisterView.as_view(), name='register'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.SubcategoriesView.as_view(), name='subcategories'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
   	path('products/new', views.CreateProductView.as_view(), name='new_product'),
   	path('products/<int:pk>/edit', views.UpdateProductView.as_view(), name='update_product'),
   	path('products/<int:pk>/delete', views.DeleteProductView.as_view(), name='delete_prodcut'),
   	path('letters/received', views.IndexRecieveLetterView.as_view(), name='received_letters'),
   	path('letters/sent', views.IndexSenderLetterView.as_view(), name='sent_letters'),
   	path('letters/<int:pk>', views.DetailLetterView.as_view(), name='letter_detail'),
   	path('letters/new', views.CreateLetterView.as_view(), name='new_letter'),
   	path('letters/<int:pk>/edit', views.UpdateLetterView.as_view(), name='update_letter'),
   	path('letters/<int:pk>/delete', views.DeleteLetterView.as_view(), name='delete_letter')
]
