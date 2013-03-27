---
layout: slide
title: "Django application structure"
published: true
data:
  x: 5000
  y: 2000
---

The actual web-requests are handled by methods called **views**. 

{% highlight python %}
from django.http import HttpResponse
def hello(request):
	return HttpResponse (
	    '''<html>
	        <body>
	            <h1>Hello, world!</h1>
	        </body>
	    </html>'''
	)
{% endhighlight %}