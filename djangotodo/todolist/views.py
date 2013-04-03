from django.shortcuts import render
from todolist.models import Task
from forms import TaskForm
from django.core.exceptions import PermissionDenied

def list(request):
	if request.method == "GET":
		form = TaskForm()
	elif request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			# make sure to return use a clean form for the resulting page
			form = TaskForm()

	else:
		raise PermissionDenied('Only GET and POST methods are allowed')

	return render(request, 'todolist/list-view.html', {
    	'tasks': Task.objects.all(),
    	'form': form
    })
