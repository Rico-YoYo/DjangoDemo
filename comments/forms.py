__author__ = 'Rico'
__date__ = '2019/9/16 13:44'

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']