from .models import Comments, Recipe
from django import forms

class AddRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'preparation_content', 'featured_image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)
