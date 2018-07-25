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


#currently simple search looking for post objects that titles contain the query word 
def search_posts(request):
	#in my search form, the get value name is 'q'
	#the request gets the value which then I used to query my database for
	#all post objects that title contains the query word
	if 'q' in request.GET:
		query = request.GET.get('q');
	searched_posts =Post.objects.filter(title__contains=query)
	return render(request, 'blog/search.html', {'posts':searched_posts})

