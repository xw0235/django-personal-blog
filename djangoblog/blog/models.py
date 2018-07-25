from django.db import models
from django.utils import timezone

# Create your models here.

'''
Post Model

Posts contain 
1. Author
2. Title
3. Description
4. Create Date
5. Publish Date
6. Image Upload

The First 5 is the same as the tutorial, I can add more later

DONT FORGET, YOU NEED TO REGISTER THE MODEL TO admin.py 

'''
class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	image = models.ImageField(upload_to='images', blank=True, null=True)

	#publish sets the publish date to the time now 
	def publish(self):
		self.published_date = timezone.now()
		#save seems to be a form of an update method 
		self.save()


	#returns the title 
	def __str__(self):
		return self.title


	#adds a property to the image
	#returns the image url, allows for better checking if image exists 
	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url	


class ProjectPost(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length = 200)
	description = models.TextField()
	link = models.CharField(max_length = 250)

	start_date = models.DateTimeField(blank=True, null=True)

	#choice field 
	#testing for now, may change to a better solution later
	#ON_GOING_CHOICES define the choices that can be selected
	ON_GOING_CHOICES = (('INC', 'Incomplete'), ('CPLT', 'Complete'),  ('DROP', 'Dropped'),)

	#on_going_project fills in the CharField with the ability to choose from the choices 
	on_going_project = models.CharField(
		max_length = 4,
		choices = ON_GOING_CHOICES,
		default = 'INC',)



