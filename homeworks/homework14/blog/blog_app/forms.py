from django import forms


class CommentForm(forms.Form):
	post = forms.IntegerField(required=True, widget=forms.HiddenInput())
	user = forms.CharField(label="User", 	max_length=32)	
	body = forms.CharField(widget=forms.Textarea)
	