from django.urls import path
from . import views

app_name = 'djangoTest'
urlpatterns = [
    path('', views.index, name='index'),
]
