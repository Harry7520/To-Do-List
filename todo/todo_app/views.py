from django.shortcuts import render,redirect
from todo_app.models import *
from datetime import datetime

# Create your views here.

def local(request):
    if request.method == "GET":
        todo = toDo.objects.all()
        return render(request, "todo.html",{'todo':todo})
    if request.method == "POST":
        todo = toDo.objects.create(
            title = request.POST.get('title'),
            create_at = datetime.now(),
        )
        todo.save()
        return redirect('/')
    
def titleDelete(request,t_id):
    todo = toDo.objects.get(id=t_id)
    todo.delete()
    return redirect('/')

def titleAllDelete(request):
    todo = toDo.objects.all()
    todo.delete()
    return redirect('/')