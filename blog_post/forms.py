from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea (attrs={'class':'col col-md-12 mb-3', 'rows':'10', 'max':'500'}))
	title = forms.CharField(widget=forms.TextInput (attrs={'class':'col col-md-12 mb-3'}))

	class Meta:
		model = Post
		fields = "__all__"


class CommentForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea (attrs={'class':'col col-md-12 mb-3', 'rows':'3', 'max':'500'}))
	# post = forms.CharField(widget=forms.HiddenInput())

	class Meta:
		model = Comment
		fields = "__all__"

	widgets = {
		'post': forms.TextInput(attrs={'value':'', 'id':'post', 'type':'hidden'})
	}
