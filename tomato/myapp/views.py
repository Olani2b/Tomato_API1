from django.http import HttpResponse
from rest_framework import viewsets
from .models import Restaurant, Recipe, Ingredient
from .serializers import RestaurantSerializer, RecipeSerializer, IngredientSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Home view that returns a welcome message
def home(request):
    return HttpResponse("Welcome to the Tomato API")

# ViewSet for Ingredient model, providing CRUD operations
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    # Custom action to filter ingredients by recipe name
    @action(detail=False, methods=['get'], url_path='by-recipe/(?P<recipe_name>[^/.]+)')
    def by_recipe(self, request, recipe_name=None):
        ingredients = Ingredient.objects.filter(recipe__name=recipe_name)
        serializer = self.get_serializer(ingredients, many=True)
        return Response(serializer.data)

    # Custom action to filter ingredients by restaurant name
    @action(detail=False, methods=['get'], url_path='by-restaurant/(?P<restaurant_name>[^/.]+)')
    def by_restaurant(self, request, restaurant_name=None):
        ingredients = Ingredient.objects.filter(recipe__restaurant__name=restaurant_name)
        serializer = self.get_serializer(ingredients, many=True)
        return Response(serializer.data)

# ViewSet for Recipe model, providing CRUD operations
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # Custom action to filter recipes by restaurant name
    @action(detail=False, methods=['get'], url_path='by-restaurant/(?P<restaurant_name>[^/.]+)')
    def by_restaurant(self, request, restaurant_name=None):
        recipes = Recipe.objects.filter(restaurant__name=restaurant_name)
        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)

    # Custom action to filter recipes by ingredient name
    @action(detail=False, methods=['get'], url_path='by-ingredient/(?P<ingredient_name>[^/.]+)')
    def by_ingredient(self, request, ingredient_name=None):
        recipes = Recipe.objects.filter(ingredients__name=ingredient_name)
        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)

# ViewSet for Restaurant model, providing CRUD operations
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    # Custom action to filter restaurants by recipe name
    @action(detail=False, methods=['get'], url_path='by-recipe/(?P<recipe_name>[^/.]+)')
    def by_recipe(self, request, recipe_name=None):
        restaurants = Restaurant.objects.filter(recipes__name=recipe_name)
        serializer = self.get_serializer(restaurants, many=True)
        return Response(serializer.data)
