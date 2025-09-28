from django.db import models # type: ignore

# Create your models here.
class Post(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text[:50]