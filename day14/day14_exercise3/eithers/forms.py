from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
	issue_a=forms.CharField(label="")
	issue_b=forms.CharField(label="")
	class Meta:
        model = Question

class CommentForm(forms.ModelForm):
	pick = forms.ChoiceField(...)