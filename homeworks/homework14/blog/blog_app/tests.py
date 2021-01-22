
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from .models import Post

def create_post(title, body, days = 0):
	return Post.objects.create(title=title, body=body, pub_date=timezone.now() + timedelta(days=days))
		

# Create your tests here.
class PostIndexViewTests(TestCase):
	def test_no_post(self):
		response = self.client.get(reverse("blog_app:index"))
		self.assertEquals(response.status_code, 200)
		self.assertContains(response, "No posts yet")
		self.assertQuerysetEqual(response.context["posts"], [])

	def test_post_exists(self):
		create_post("Test title", "Test body")
		response = self.client.get(reverse("blog_app:index"))
		self.assertQuerysetEqual(response.context["posts"], ["<Post: Test title>"])


class PostDetailVIewTests(TestCase):
 	def test_future_post(self):
 		post = create_post("Test title", "Test body", 1)
 		response = self.client.get(reverse("blog_app:detail", args=(post.id,)))
 		self.assertEquals(response.status_code, 404) 			

 	def test_past_post(self):
 		post = create_post("Test title", "Test body", -1)
 		response = self.client.get(reverse("blog_app:detail", args=(post.id,)))
 		self.assertEquals(response.status_code, 200)
 		self.assertContains(response, post) 			
