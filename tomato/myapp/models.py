from django.db import models

# Ingredient model representing individual ingredients
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Recipe model representing a recipe, with a many-to-many relationship to ingredients
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

# Restaurant model representing a restaurant, with a many-to-many relationship to recipes
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name
