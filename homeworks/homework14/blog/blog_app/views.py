from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment

# Create your views here.
def index(request):
	posts = Post.objects.order_by("pub_date")
	return render(request, "blog_app/index.html", {"posts": posts})

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, "blog_app/detail.html", {"post": post})

def create_comment(request, post_id):
	return HttpResponseRedirect(reverse('blog_app:index'))