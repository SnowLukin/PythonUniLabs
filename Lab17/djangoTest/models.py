from django.db import models


class Chefs(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Recipes(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    cost = models.IntegerField()

    def __str__(self):
        return self.title

