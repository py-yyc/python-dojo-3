---
layout: slide
title: "The structure of a Django project"
published: true
data:
  x: 4000
  y: 2000
---

{% highlight python %}
# Remember the method decorators from Flask?
@app.route("/")
def hello():
    return "Hello World!"
{% endhighlight %}

The urls.py is a file containing these url-to-funtion mappings for the project

{% highlight python %}
from django.conf.urls import patterns, include
urlpatterns = patterns('',
	url(r'^$', 'todo.views.hello'),
)
{% endhighlight %}