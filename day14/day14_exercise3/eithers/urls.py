from django.urls import path
from . import views

app_name='eithers'
urlpattern =[
    path('', views.index, name='index'),
    path('create/',views.create,name='create'),
    path('random/', views.random, name='random'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('<int:question_pk>/comment/', views.comment_create, name='comment_create'),

]