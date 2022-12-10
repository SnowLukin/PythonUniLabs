from django.contrib import admin
from .models import Chef, Recipe, Ingredient, Article, Post


admin.site.register(Chef)
admin.site.register(Article)
admin.site.register(Post)
admin.site.register(Recipe)
admin.site.register(Ingredient)
