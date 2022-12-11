from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Chef, Post, Article, Ingredient, Recipe
from django.urls import reverse
from django.shortcuts import redirect


def index(request):
    return render(request, 'djangoTest/index.html', {})


def chefs(request):
    objs = Chef.objects.order_by('-name')
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/chefs.html', context)


def add_chef(request):
    objs = Chef.objects.order_by('-name')
    chef_id = len(objs)
    name = request.POST['first']
    surname = request.POST['last']
    entity = Chef(name=name, surname=surname)
    entity.id = chef_id     # to be able to edit entity in future
    entity.save()
    print(entity.id)
    return redirect(reverse('djangoTest:chefs'))


def delete_chef(request, entity_id):
    entity = Chef.objects.get(id=entity_id)
    entity.delete()
    return redirect(reverse('djangoTest:chefs'))


def edit_chef(request):
    entity_id = request.POST['edit_id']
    # Would be cool to check before updating but nah
    entity = Chef.objects.get(id=entity_id)
    entity.name = request.POST['edit_first']
    entity.surname = request.POST['edit_last']
    entity.save()
    return redirect(reverse('djangoTest:chefs'))


def posts(request):
    objs = Post.objects.order_by('-title')
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/posts.html', context)


def add_post(request):
    objs = Post.objects.order_by('-title')
    entity_id = len(objs)
    title = request.POST['first']
    body = request.POST['last']
    entity = Post(title=title, body=body)
    entity.id = entity_id     # to be able to edit entity in future
    entity.save()
    return redirect(reverse('djangoTest:posts'))


def delete_post(request, entity_id):
    entity = Post.objects.get(id=entity_id)
    entity.delete()
    return redirect(reverse('djangoTest:posts'))


def edit_post(request):
    entity_id = request.POST['edit_id']
    # Would be cool to check before updating but nah
    entity = Post.objects.get(id=entity_id)
    entity.title = request.POST['edit_first']
    entity.body = request.POST['edit_last']
    entity.save()
    return redirect(reverse('djangoTest:posts'))


def articles(request):
    objs = Article.objects.order_by('-title')
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/articles.html', context)


def add_article(request):
    objs = Article.objects.order_by('-title')
    entity_id = len(objs)
    title = request.POST['first']
    body = request.POST['last']
    entity = Article(title=title, body=body)
    entity.id = entity_id     # to be able to edit entity in future
    entity.save()
    return redirect(reverse('djangoTest:articles'))


def delete_article(request, entity_id):
    entity = Article.objects.get(id=entity_id)
    entity.delete()
    return redirect(reverse('djangoTest:articles'))


def edit_article(request):
    entity_id = request.POST['edit_id']
    # Would be cool to check before updating but nah
    entity = Article.objects.get(id=entity_id)
    entity.title = request.POST['edit_first']
    entity.body = request.POST['edit_last']
    entity.save()
    return redirect(reverse('djangoTest:articles'))


def ingredients(request):
    objs = Ingredient.objects.order_by('-name')
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/ingredients.html', context)


def add_ingredient(request):
    objs = Ingredient.objects.order_by('-name')
    entity_id = len(objs)
    name = request.POST['first']
    cost = int(request.POST['last'])
    entity = Ingredient(name=name, cost=cost)
    entity.id = entity_id     # to be able to edit entity in future
    entity.save()
    return redirect(reverse('djangoTest:ingredients'))


def delete_ingredient(request, entity_id):
    entity = Ingredient.objects.get(id=entity_id)
    entity.delete()
    return redirect(reverse('djangoTest:ingredients'))


def edit_ingredient(request):
    entity_id = request.POST['edit_id']
    # Would be cool to check before updating but nah
    entity = Post.objects.get(id=entity_id)
    entity.name = request.POST['edit_first']
    entity.cost = int(request.POST['edit_last'])
    entity.save()
    return redirect(reverse('djangoTest:ingredients'))


def recipes(request):
    objs = Recipe.objects.order_by('-title')
    context = {
        'objs': objs,
    }
    return render(request, 'djangoTest/recipes.html', context)


def add_recipe(request):
    objs = Recipe.objects.order_by('-title')
    entity_id = len(objs)
    title = request.POST['first']
    body = request.POST['second']
    cost = request.POST['third']
    entity = Recipe(title=title, body=body, cost=cost)
    entity.id = entity_id     # to be able to edit entity in future
    entity.save()
    return redirect(reverse('djangoTest:recipes'))


def delete_recipe(request, entity_id):
    entity = Recipe.objects.get(id=entity_id)
    entity.delete()
    return redirect(reverse('djangoTest:recipes'))


def edit_recipe(request):
    entity_id = request.POST['edit_id']
    # Would be cool to check before updating but nah
    entity = Recipe.objects.get(id=entity_id)
    entity.title = request.POST['edit_first']
    entity.body = request.POST['edit_second']
    entity.cost = request.POST['edit_third']
    entity.save()
    return redirect(reverse('djangoTest:recipes'))
