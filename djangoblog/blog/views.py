from django.shortcuts import render


# Create your views here.
#views connect backend to frontend, allows python code to move to static HTML

def post_list(request):
	#renders the html to be displayed
	return render(request, 'blog/base.html', {})

def about_page(request):
	#renders the about page to be displayed
	return render(request, 'blog/about.html', {})
