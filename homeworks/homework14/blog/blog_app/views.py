from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post, Comment

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
		return Post.objects.order_by("-pub_date")

class DetailView(generic.DetailView):
	model = Post
	template_name = "blog_app/detail.html"

def create_comment(request, post_id):
	return HttpResponseRedirect(reverse('blog_app:index'))