from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# Create your views here.
@require_safe
def index(request):
    
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request, 'todos/index.html',context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method=='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author=request.user
            todo.save()
            return redirect('todos:index')
    else:
        form=TodoForm()
    context={
        'form':form,
    }
    return render(request, 'todos/create.html', context)

@require_POST
def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user==todo.author:
            if todo.completed==False:
                todo.completed=True
            else:
                todo.completed=False
            todo.save()
            return redirect('todos:index')
    return redirect('accounts:login')

@require_POST
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user==todo.author:
            todo.delete()
            return redirect('todos:index')
    return redirect('todos:index')