from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

@require_safe
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)
def detail(request):
    pass
def create(request):
    pass
def random(request):
    questions=Question.objects.values('pk')# select id from eithers_question
# Question.object.filter(id__exact=14).value()... # select * from eithers_question where id=14
    pkList=[]
    for value in questions:
        pkList.append(value['pk'])
    selected_pk=random.choice(pkList)
    
# Create your views here.
