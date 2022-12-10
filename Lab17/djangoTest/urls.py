from django.urls import path
from . import views

app_name = 'djangoTest'
urlpatterns = [
    path('', views.index, name='index'),
    path('chefs', views.chefs, name='chefs'),
    path('posts', views.posts, name='posts'),
    path('articles', views.articles, name='articles'),
    path('ingredients', views.ingredients, name='ingredients'),
    path('recipes', views.recipes, name='recipes'),
    path('delete_chef/<int:entity_id>', views.delete_chef, name='delete_chef'),
    path('add_chef/', views.add_chef, name='add_chef'),
]