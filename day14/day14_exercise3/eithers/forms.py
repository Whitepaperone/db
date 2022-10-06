from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
	issue_a=forms.CharField(label="RED TEAM")
	issue_b=forms.CharField(label="BLUE TEAM")
	class Meta:
        model = Question

class CommentForm(forms.ModelForm):
	CHOICES=(
		()
	)
	pick = forms.ChoiceField(choices=CHOICES)
	class Meta:
        model = Comment
