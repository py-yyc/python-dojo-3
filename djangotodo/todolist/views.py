from django.shortcuts import render
from todolist.models import Task

def list(request):
    return render(request, 'todolist/list-view.html', {
    	'tasks': Task.objects.all()
    })
