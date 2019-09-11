from django import forms
from .models import Recipe

class AuthorForm(forms.Form):
    author_name = forms.CharField(max_length=20)
    author_bio = forms.CharField(widget=forms.Textarea)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author', 'description', 'time_req', 'instructions']
