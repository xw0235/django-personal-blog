from django.db import models
from django.utils import timezone
import os

# Create your models here.

'''
Post Model

Posts contain 
1. Author
2. Title
3. Description
4. Post Type
5. Create Date
6. Publish Date
7. Image Upload


The First 5 is the same as the tutorial

Dont forget to register models to admin.py 

'''

#Post model, represents post within the blog
class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()

	#Indicates what type of post
	POST_TYPE_CHOICES = (('BLG', 'Blog'), ('ABT', 'About'))
	post_type = models.CharField(
		max_length = 4,
		choices = POST_TYPE_CHOICES,
		default='BLG',)


	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	image = models.ImageField(upload_to='images', blank=True, null=True)



	#publish sets the publish date to the time now 
	def publish(self):
		self.published_date = timezone.now()
		#save seems to be a form of an update method 
		self.save()

	def get_post_type(self):
		return self.get_post_type_display()


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




#highlights posts
class Highlight(models.Model):
	header = models.CharField(max_length=200)
	link = models.CharField(max_length=250, blank=True, default='')

	#can add more highlight choices here 
	HIGHLIGHT_CHOICES = (('POST', 'Post'), ('PROJ','Projects'), ('RESU','Resume'), ('ABOT','About') )
	highlight_type = models.CharField(
		max_length = 4,
		choices = HIGHLIGHT_CHOICES,
		default='POST',)

	#returns the header
	def __str__(self):
		return self.header


#Document class for files 
#allows blogger to upload documents to site
#currently used in resume page 
class Document(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	#fileField, will be stored in static/media/files
	doc = models.FileField(upload_to='files')

	#returns the title
	def __str__(self):
		return self.title

	def get_file_type(self):
		filename, file_extension = os.path.splitext(self.doc.url)
		return file_extension












