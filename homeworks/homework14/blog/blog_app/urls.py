from django.urls import path
from . import views

app_name = "blog_app"
urlpatterns = [	
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:post_id>/create_comment/', views.create_comment, name='create_comment')
]
