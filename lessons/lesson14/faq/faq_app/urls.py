from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "faq"
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('register', views.RegisterView.as_view(), name='register'),
	path('question/new', views.CreateQuestion.as_view(), name='new_question'),
	path('question/<int:pk>', views.UpdateQuestion.as_view(), name='update_quesdtion'),
	path('question/delete/<int:pk>', views.DeleteQuestion.as_view(), name='delete_question'),
]

