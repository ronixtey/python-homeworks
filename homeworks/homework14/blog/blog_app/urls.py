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
	path('register/', views.RegisterView.as_view(), name='register'),
	path('new/', views.CreatePostView.as_view(), name='new_post'),
	path('<int:pk>/edit', views.UpdatePostView.as_view(), name='edit_post'),
	path('<int:pk>/delete', views.DeletePostView.as_view(), name='delete_post'),

]

