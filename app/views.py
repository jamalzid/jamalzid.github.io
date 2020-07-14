from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'index.html', context)


def edite(request,id):
    task=get_object_or_404(Task,id=id)
    form = TaskForm(instance=task)
    if request.method =='POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form,
    }
    return render(request, 'edite.html', context)


def delete(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    
    context={
        'task':task,
    }
    return render(request, 'delete.html', context)
