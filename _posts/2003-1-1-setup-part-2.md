---
layout: slide
title: "Installation/Setup - part 2"
published: true
data:
  x: 2000
  y: 2000
---

Now clone the project repo:

{% highlight bash %}
$ git clone git@github.com:py-yyc/python-dojo-3.git
$ cd python-dojo-3
{% endhighlight %}

Make your team branch:

{% highlight bash %}
$ git checkout -b team_awesome
{% endhighlight %}

Don't push to the master branch!

{% highlight bash %}
$ git commit -m "Awesome feature added!"
$ git push origin team_awesome
{% endhighlight %}