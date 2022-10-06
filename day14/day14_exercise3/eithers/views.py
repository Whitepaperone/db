from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

# Create your views here.
questions=Question.objects.values('pk')# select id from eithers_question
# Question.object.filter(id__exact=14).value()... # select * from eithers_question where id=14
pkList=[]
for value in questions:
    pkList.append(value['pk'])
selected_pk=random.choice(pkList)