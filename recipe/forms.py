from .models import Comments, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'author', 'ingredients', 'preparation_content', 'featured_image', 'status',]
