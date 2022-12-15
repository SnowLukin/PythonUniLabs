from django.urls import path
from . import views
from django.urls import include, path

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
    path('edit_chef/', views.edit_chef, name='edit_chef'),

    path('delete_post/<int:entity_id>', views.delete_post, name='delete_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/', views.edit_post, name='edit_post'),

    path('delete_article/<int:entity_id>', views.delete_article, name='delete_article'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/', views.edit_article, name='edit_article'),

    path('delete_ingredient/<int:entity_id>', views.delete_ingredient, name='delete_ingredient'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('edit_ingredient/', views.edit_ingredient, name='edit_ingredient'),

    path('delete_recipe/<int:entity_id>', views.delete_recipe, name='delete_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit_recipe/', views.edit_recipe, name='edit_recipe'),

    path("register", views.register_request, name="register")
]