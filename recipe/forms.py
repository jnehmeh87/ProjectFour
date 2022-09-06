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

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here...'}),
            'slug' : forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write down all the Ingredients needed in this area...'}),
            'preparation_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a detailed description for the recipe in this area...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
