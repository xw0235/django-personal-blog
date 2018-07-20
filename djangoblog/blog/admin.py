from django.contrib import admin
from .models import Post
from .models import ProjectPost

# Register your models here.
#dont forget to import the model here
admin.site.register(Post)
admin.site.register(ProjectPost)
