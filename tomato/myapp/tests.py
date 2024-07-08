from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Restaurant, Recipe, Ingredient

class IngredientTests(APITestCase):
    def test_create_ingredient(self):
        url = reverse('ingredient-list')
        data = {'name': 'Tomato'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient.objects.count(), 1)
        self.assertEqual(Ingredient.objects.get().name, 'Tomato')

class RecipeTests(APITestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name='Tomato')

    def test_create_recipe(self):
        url = reverse('recipe-list')
        data = {
            'name': 'Tomato Soup',
            'ingredients': [{'name': 'Tomato'}]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Recipe.objects.get().name, 'Tomato Soup')

class RestaurantTests(APITestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name='Tomato')
        self.recipe = Recipe.objects.create(name='Tomato Soup')
        self.recipe.ingredients.add(self.ingredient)

    def test_create_restaurant(self):
        url = reverse('restaurant-list')
        data = {
            'name': 'Tomato Bistro',
            'recipes': [{'name': 'Tomato Soup', 'ingredients': [{'name': 'Tomato'}]}]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name, 'Tomato Bistro')
