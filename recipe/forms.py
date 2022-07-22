from .models import Comments, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)
