from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Chef, Post, Article, Ingredient, Recipe
from django.urls import reverse
from django.shortcuts import redirect

def index(request):
    chefsObj = Chef.objects
    context = {
        'chefsObj': chefsObj,
    }
    return render(request, 'djangoTest/index.html', {})


def chefs(request):
    objs = Chef.objects.order_by('-name')
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/chefs.html', context)


def add_chef(request):
    objs = Chef.objects.order_by('-name')
    # chef_id = len(objs)
    name = request.POST['first']
    surname = request.POST['last']
    entity = Chef(name=name, surname=surname)
    entity.save()
    return redirect(reverse('djangoTest:chefs'))


def delete_chef(request, entity_id):
    entity = Chef.objects.get(id=entity_id)
    entity.delete()
    return redirect(reverse('djangoTest:chefs'))
    # return HttpResponseRedirect(reverse('djangoTest/chefs'))


def posts(request):
    objs = list(Post.objects)
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/posts.html', context)


def articles(request):
    objs = list(Article.objects)
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/articles.html', context)


def ingredients(request):
    objs = list(Ingredient.objects)
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/ingredients.html', context)


def recipes(request):
    objs = list(Recipe.objects)
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/recipes.html', context)
