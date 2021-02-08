from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# from django.contrib.auth import authenticate, login

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
	# автоматом поставит "post_detail.html"
	# template_name = "blog_app/detail.html"

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
		# user = authenticate(self.request, username=self.request.POST['username'], password=self.request.POST['password1'])
		# login(self.request, self.request.user)
		
		form.save()
		return super(RegisterView, self).form_valid(form)

	def form_invalid(self, form):
		return super(RegisterView, self).form_invalid(form)


class CreatePostView(generic.edit.CreateView):
	model = Post
	template_name = "blog_app/new_post.html"
	fields = ['title', 'body']

	def form_valid(self, form):
	
		form.instance.user = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse("blog_app:index")


class UpdatePostView(generic.edit.UpdateView):
	model = Post
	template_name = "blog_app/update_post.html"
	fields = ['title', 'body']


	def get_success_url(self):
		return reverse("blog_app:index")

class DeletePostView(generic.edit.DeleteView):
	model = Post
	template_name = "blog_app/delete_post.html"

	def get_success_url(self):
		return reverse("blog_app:index")
		



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
