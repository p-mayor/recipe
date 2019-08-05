from django.shortcuts import get_object_or_404, render

from .models import Recipe

def index(request):
    latest_recipe_list = Recipe.objects.order_by('title')
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'recipe/index.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe/detail.html', {'recipe': recipe})

def author(request, recipe_id):
    return HttpResponse("The author page for %s." % recipe_id)