from django.shortcuts import render
from .models import Post
from django.utils import timezone


# Create your views here.
#views connect backend to frontend, allows python code to move to static HTML

def post_list(request):

	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')





	#renders the html to be displayed
	return render(request, 'blog/posts.html', {'posts':posts})

def about_page(request):
	#renders the about page to be displayed
	return render(request, 'blog/about.html', {})


def search_posts(request):
	query = self.request.GET.get('q');
	searched_posts =Post.objects.filter(name__contains=q)
	return render(request, 'blog/posts.html', {'posts':searched_posts})

