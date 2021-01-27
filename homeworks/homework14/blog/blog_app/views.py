from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post, Comment
from .forms import RegistrationForm, CommentForm

# Create your views here.
# def index(request):
# 	posts = Post.objects.order_by("pub_date")
# 	return render(request, "blog_app/index.html", {"posts": posts})

# def detail(request, post_id):
# 	post = get_object_or_404(Post, pk=post_id)
# 	return render(request, "blog_app/detail.html", {"post": post})


class IndexView(generic.ListView):
	template_name = "blog_app/index.html"
	context_object_name = "posts"

	def get_queryset(self):
		return Post.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")


class DetailView(generic.DetailView):
	model = Post
	template_name = "blog_app/detail.html"

	def get_queryset(self):
		return Post.objects.filter(pub_date__lte=timezone.now())

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["form"] = CommentForm()
		return context

class RegisterView(generic.edit.FormView):
	form_class = RegistrationForm
	success_url = "/login"
	template_name = "registration/register.html"

	def form_valid(self, form):
		form.save()
		return super(RegisterView, self).form_valid(form)

	def form_invalid(self, form):
		return super(RegisterView, self).form_invalid(form)


def create_comment(request, post_id):	
	if(request.method == "POST"):
		form = CommentForm(request.POST)
		if(form.is_valid()):
			#post = get_object_or_404(Post, pk=post_id)
			form.post = post_id 
			return HttpResponseRedirect(reverse('blog_app:index'))
		else: 
			form = CommentForm()

		return render(request, "blog_app/detail.html", {"form": form})
