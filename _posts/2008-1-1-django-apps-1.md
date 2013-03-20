---
layout: slide
title: "But where does my code go?"
published: true
data:
  x: 5000
  y: 0
---

Introducing... Django applications

Django applications are modules of code that contain a single feature. Django projects contain many such applications.

{% highlight bash %}
$ ./manage.py startapp todolist
$ tree todolist/
todolist/
├── __init__.py
├── models.py
├── tests.py
└── views.py
{% endhighlight %}