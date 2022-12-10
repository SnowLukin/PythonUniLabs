from django.contrib import admin
from .models import Chefs, Recipes, Ingredients, Articles, Posts


admin.site.register(Chefs, Articles, Posts, Recipes, Ingredients)


