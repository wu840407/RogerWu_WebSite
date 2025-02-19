# blog/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '您的名字'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '請留下您的意見'}),
        }
