from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Recipe, Author
from .forms import AuthorForm

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['author_name']
            bio = form.cleaned_data['author_bio']
            a = Author(name=name,bio=bio)
            a.save()
            return HttpResponseRedirect('/')
    else:
        form = AuthorForm()
    return render(request, 'recipe/add_author.html', {'form':form})

def index(request):
    latest_recipe_list = Recipe.objects.order_by('title')
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'recipe/index.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe/detail.html', {'recipe': recipe})

def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author_recipe_list = Recipe.objects.filter(author=author_id)
    return render(request, 'recipe/author.html', 
        {'author': author, 'author_recipe_list':author_recipe_list}
    )