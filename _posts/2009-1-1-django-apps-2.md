---
layout: slide
title: "Django application structure"
published: true
data:
  x: 5000
  y: 1000
---

Django comes bundled with its own ORM (Object Relation Mapping) system. You don't have to use it but it is HIGHLY RECOMMENDED.

Models.py contains the object representations of your database tables.

{% highlight python %}
from django.db import models
class Task(models.Model):
	description = models.TextField()
	# more fields like a done-flag, date etc. 
	# can be added to make this awesome
{% endhighlight %}