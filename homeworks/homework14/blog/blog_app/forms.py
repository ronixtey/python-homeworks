from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class CommentForm(forms.Form):
	post = forms.IntegerField(required=True, widget=forms.HiddenInput())
	user = forms.CharField(label="User", 	max_length=32)	
	body = forms.CharField(widget=forms.Textarea)


	