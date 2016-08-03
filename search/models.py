from django.db import models

# Create your models here.
class acticle(models.Model):
	name = models.CharField(max_length=256)
	intro = models.TextField(default='')

	def __unicode__(self):
		return self.name