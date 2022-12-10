from django.shortcuts import render, get_object_or_404
from .models import Chefs, Posts, Articles, Ingredients, Recipes


def index(request):
    chefsObj = Chefs.objects
    context = {
        'chefsObj': chefsObj,
    }
    return render(request, 'djangoTest/index.html', context)


def chefs(request):
    objs = Chefs.objects
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/chefs.html', context)


def posts(request):
    objs = Posts.objects
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/posts.html', context)


def articles(request):
    objs = Articles.objects
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/articles.html', context)


def ingredients(request):
    objs = Ingredients.objects
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/ingredients.html', context)


def recipes(request):
    objs = Recipes.objects
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/recipes.html', context)
