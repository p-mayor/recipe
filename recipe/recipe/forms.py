from django import forms

class AuthorForm(forms.Form):
    author_name = forms.CharField(max_length=20)
    author_bio = forms.CharField(widget=forms.Textarea)