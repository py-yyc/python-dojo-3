from django.db import models
from django.contrib import admin

class Task(models.Model):
    description = models.TextField(max_length=200)

    def __unicode__(self):
    	return self.description

admin.site.register(Task)