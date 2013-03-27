---
layout: slide
title: "Django application structure"
published: true
data:
  x: 5000
  y: 3000
---

But nobody wants to write complicated HTML using a string in a function. For this, Django has its own templating language.

{% highlight html %}
<html>
	<body><h1>Hello {% raw %}{{ username }}{% endraw %}</h1></body>
</html>
{% endhighlight %}

{% highlight python %}
from django.shortcuts import render
def hello(request):
	return render(request, 'todo/hello-template.html', {
	    'username': request.user.username
	})
{% endhighlight %}