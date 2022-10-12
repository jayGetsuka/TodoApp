from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todoWebApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone



# Create your views here.
def index(request):
    return render(request, 'index.html', {'todo': Todo.objects.all()})

def addTodo(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        date = request.POST['date']

        todo = Todo(title=title, description=desc, deadline=date)
        todo.save()

        return redirect('/')
    else:
        return render(request, 'addtodo.html')

def editTodo(request, id):
    if request.method == "POST":
        todo = Todo.objects.get(id=id)
        todo.title = request.POST['title']
        todo.description = request.POST['desc']
        todo.deadline = request.POST['date']
        todo.done = request.POST['status']

        todo.save()

        return redirect('/')

    else:
        todo = Todo.objects.get(id=id)
        return render(request, 'edittodo.html', {'todo': todo})
