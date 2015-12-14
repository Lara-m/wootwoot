from django.db import models	
from django.contrib import admin	

class URLPost(models.Model):
	name = models.CharField(max_length=20)
	body = models.CharField(max_length=110)
	#timestamp = models.DateTimeField()
	@classmethod
	def create(cls, n, u):
		name = cls(name=n)
		body = cls(body=u)
		return self


class AdminPost(admin.ModelAdmin): 
	list_display = ('name', 'timestamp')


admin.site.register(URLPost)