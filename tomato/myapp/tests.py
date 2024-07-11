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
        self.recipe1 = Recipe.objects.create(name='Tomato Soup')
        self.recipe1.ingredients.add(self.ingredient)
        self.recipe2 = Recipe.objects.create(name='Tomato Salad')
        self.recipe2.ingredients.add(self.ingredient)

        self.restaurant = Restaurant.objects.create(name='Tomato Bistro')
        self.restaurant.recipes.add(self.recipe1, self.recipe2)

    def test_create_restaurant(self):
        url = reverse('restaurant-list')
        data = {
            'name': 'Tomato Bistro',
            'recipes': [{'name': 'Tomato Soup', 'ingredients': [{'name': 'Tomato'}]}]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 2)  # There should be 2 restaurants now
        self.assertEqual(Restaurant.objects.latest('id').name, 'Tomato Bistro')

    def test_restaurant_recipe_count(self):
        url = reverse('restaurant-detail', args=[self.restaurant.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['recipes']), 2)

    def test_count_recipes_for_tomato_bistro(self):
        
        restaurant = Restaurant.objects.get(name='Tomato Bistro')
        self.assertEqual(restaurant.recipes.count(), 2)
