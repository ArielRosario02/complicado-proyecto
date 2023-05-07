
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def projects(request):
    # projects=list(Project.objects.values())
    projects = Project.objects.all()

    return render(request, 'projects.html', {
        'projects': projects
    })


def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'titulo': title})


def about(request):
    username = 'Ariel Rosario!'
    return render(request, 'about.html', {
        'username': username
    })


def muela(request, username):
    return HttpResponse('<h1>Hola Querido </h1>')


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    
    else:
    
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')
