from django.db import models

# Create your models here.

class Articles(models.Model):
	source = models.Charfield(max_length = 100)
	author = models.Charfield(max_length = 100)
	title = models.Charfield(max_length = 100)
	description = models.TextField()
	url = models.Charfield(max_length = 1000)
	urlToImage = models.Charfield(max_length = 1000)
	publishedAt = models.Charfield(max_length = 100)
	content = models.TextField()

	def __str__(self):
		return self.title
