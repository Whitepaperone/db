# todos/urls.py

```python
from django.urls import path
from . import views

app_name='todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.update, name='update'),
    path('<int:pk>/delete', views.delete,name='delete'),
]
e'),
]

```

# todos/views.py

```python
...
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
      {% if request.user == todo.author %}
        {% if todo.completed%}
          <form action="{% url 'todos:update' todo.pk%}" method="POST">
            {% csrf_token %}
            <input type="submit" value="취소하기">
          </form>
        {% else %}
        <form action="{% url 'todos:update' todo.pk%}" method="POST">
          {% csrf_token %}
          <input type="submit" value="완료하기">
        </form>
        {% endif%}
        <form action="{% url 'todos:delete' todo.pk%}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제하기">
        </form>
      {% endif %}
    </li>
    {% empty %}
    <p>작성된 글이 없습니다.</p>
  {% endfor %}
{% endif %}
{% endblock content %}

ock content %}


```


