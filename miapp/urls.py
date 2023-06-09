from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name= "index"),
    path('about/', views.about, name= "about"),
    path('muela/<str:username>', views.muela, name= "muela"),
    path('tasks/', views.tasks, name= "tasks"),
    path('projects/', views.projects, name= "projects"),
    path('create_task/', views.create_task, name= "create_task"), 
    path('create_project/', views.create_project, name= "create_project"),
]
