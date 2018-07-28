from django.contrib import admin
from .models import Post
from .models import ProjectPost
from .models import Highlight
from .models import Document


# Register your models here.
#dont forget to import the model here
admin.site.register(Post)
admin.site.register(ProjectPost)
admin.site.register(Highlight)
admin.site.register(Document)
