from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "blog_app"
urlpatterns = [	
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:post_id>/create_comment/', views.create_comment, name='create_comment'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('register/', views.RegisterView.as_view(), name='register')
]
