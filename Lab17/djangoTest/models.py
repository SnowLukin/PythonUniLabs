from django.db import models


class Chef(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    cost = models.IntegerField()

    def __str__(self):
        return self.title

