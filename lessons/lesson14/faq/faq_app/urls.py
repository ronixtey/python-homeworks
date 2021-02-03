from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "faq"
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('question/new', views.CreateQuestion.as_view(), name='new_question')
]

