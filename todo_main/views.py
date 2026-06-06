from django.template import context
from todo.models import Task
from django.shortcuts import render

# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-update_at')
    completed_tasks = Task.objects.filter(is_completed=True)
    context ={
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'home.html', context)