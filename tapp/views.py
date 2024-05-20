# todoapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoForm

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()

    todos = TodoItem.objects.all()
    return render(request, 'index.html', {'form': form, 'todos': todos})

def list(request):
    todos = TodoItem.objects.all()
    return render(request, 'list.html', {'todos': todos})
