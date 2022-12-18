from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm,CommentForm

# Create your views here.
def index(request):
	if request.user.is_authenticated:
	    template = 'list.html'
	    posts = Post.objects.all()
	    context = {
	         'posts': posts,
	    }
	    return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))


def add_post(request):
	if request.user.is_authenticated:
		template = "add_post.html"

		if request.method == "POST":
			form = PostForm(request.POST)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect(reverse_lazy('blog_post:index'))
		else:
			context = {
				'post_form': PostForm(),
			}
			return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))


def view_post(request, post_id):
	if request.user.is_authenticated:
		template = "view_post.html"
		post = Post.objects.get(id=int(post_id))
		comments = Comment.objects.filter(post=post_id).order_by('-created_date')


		if request.method == "POST":		
			form= CommentForm(request.POST)

			if form.is_valid():		
				form.save()
			return (HttpResponseRedirect('/view_post/'+ post_id))
		else:
			context = {
				'post': post,
				'comment_form': CommentForm(),
				'comments' : comments
			}
		
		return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))


def update_post(request, post_id):

	if request.user.is_authenticated:
		template = "update_post.html"
		post = Post.objects.get(id=int(post_id))

		if request.method == "POST":
			form = PostForm(request.POST, instance=post)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect(reverse_lazy('blog:index'))
		else:
			context = {
				'post_form': PostForm(instance=post),
			}
			return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))

def delete_comment(request,  post_id, comment_id):
	if request.user.is_authenticated:
		comment = Comment.objects.get(id=int(comment_id))
		comment.delete()
		return HttpResponseRedirect('/view_post/'+ post_id)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))



def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))
