from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class QuestionIndexViewTests(TestCase):
	def test_no_post(self):
		response = self.client.get(reverse("blog_app:index"))
		self.assertEquals(response.status_code, 200)
		self.assertContains(response, "No posts yet")
		self.assertQuerysetEqual(response.context["posts"], [])

	def test_post_exists(self):
		Post.objects.create(title="Test title", body="Test body")
		
		response = self.client.get(reverse("blog_app:index"))
		self.assertQuerysetEqual(response.context["posts"], ["<Post: Test title>"])