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

Dont forget to register models to admin.py 

'''

#Post model, represents post within the blog
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


#project posts
class ProjectPost(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length = 200)
	description = models.TextField()
	link = models.CharField(max_length = 250)

	start_date = models.DateTimeField(blank=True, null=True)

	#choice field 
	#ON_STATUS_CHOICES define the choices that can be selected
	ON_STATUS_CHOICES = (('INC', 'Incomplete'), ('CPLT', 'Complete'),  ('DROP', 'Dropped'),)

	#on_going_project fills in the CharField with the ability to choose from the choices 
	status = models.CharField(
		max_length = 4,
		choices = ON_STATUS_CHOICES,
		default = 'INC',)


	#Project type choice field
	PROJECT_TYPE_CHOICES = (('GRP', 'Group'), ('INDV', 'Individual'))
	project_type = models.CharField(
		max_length = 4,
		choices = PROJECT_TYPE_CHOICES,
		default = 'INDV',)


	#returns the title 
	def __str__(self):
		return self.title

	#gets the status as complete word, not abbreviation
	def get_status(self):
		return self.get_status_display()

	def get_type(self):
		return self.get_project_type_display()

	



#about page posts 
#simple post 
class AboutPost(models.Model):
	header = models.CharField(max_length = 200)
	text = models.TextField()

	#returns the title 
	def __str__(self):
		return self.header





