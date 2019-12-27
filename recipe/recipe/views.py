from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test


from .models import Recipe, Author
from .forms import AuthorForm, RecipeForm

@login_required
def add_author(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = AuthorForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['author_name']
                bio = form.cleaned_data['author_bio']
                a = Author(name=name,bio=bio, user=request.user)
                a.save()
                return HttpResponseRedirect('/')
        else:
            form = AuthorForm()
        return render(request, 'recipe/add_author.html', {'form':form})
    else:
        messages.info(request, 'You must be staff to add an author.')
        return HttpResponseRedirect('/')

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RecipeForm()
    return render(request, 'recipe/add_recipe.html', {'form':form})


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

# ref: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'recipe/signup.html', {'form': form})
