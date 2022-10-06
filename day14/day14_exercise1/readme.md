# pratice1/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('todos/', include('todos.urls')),
    path('admin/', admin.site.urls),
]
```

# practice/settings.py

```python
...
INSTALLED_APPS = [
    'accounts',
    'todos',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
...
```

# todos/models.py

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    completed=models.BooleanField(default=False)

```

# todos/forms.py

```python
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        exclude=('author',)
```

# todos/urls.py

```python
from django.urls import path
from . import views

app_name='todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]

```

# todos/views.py

```python
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
 'todos/create.html', context)

```

# todos/templates/todos/create.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>CREATE</h1>
<form action="" method="post">
  {% csrf_token %}
  {{ form.as_p}}
  <input type="submit">
</form>
{% endblock content %}
```

# todos/templates/todos/index.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>Todos</h1>
<hr>
{% if request.user.is_authenticated %}
  <a href="{% url 'todos:create' %}">CREATE</a>
  <ul>
  {% for todo in todos %}
    <li>
      {{ todo.author }} - {{todo.title}}
    </li>
    {% empty %}
    <p>작성된 글이 없습니다.</p>
  {% endfor %}
{% endif %}
{% endblock content %}


```


