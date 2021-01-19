from django.urls import path
from . import views

app_name = "blog_app"
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:post_id>/', views.detail, name='detail'),
	path('<int:post_id>/create_comment/', views.create_comment, name='create_comment')
]
