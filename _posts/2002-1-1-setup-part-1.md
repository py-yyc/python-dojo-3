---
layout: slide
title: "Installation/Setup - part 1"
published: true
data:
  x: 2000
  y: 1000
---

I recommend you make and use a virtual environment:

{% highlight bash %}
$ cd /path/to/virtualenvs
$ virtualenv django-demo
$ cd django-demo
$ source bin/activate
{% endhighlight %}

Now install Django:

{% highlight bash %}
$ pip install Django
{% endhighlight %}