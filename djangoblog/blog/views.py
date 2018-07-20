from django.shortcuts import render


# Create your views here.
#views connect backend to frontend, allows python code to move to static HTML

def post_list(request):
	#renders the html which displays 
	return render(request, 'blog/base.html', {})
