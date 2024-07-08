from rest_framework import serializers
from .models import Restaurant, Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(**ingredient_data)
            recipe.ingredients.add(ingredient)
        return recipe

class RestaurantSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'

    def create(self, validated_data):
        recipes_data = validated_data.pop('recipes')
        restaurant = Restaurant.objects.create(**validated_data)
        for recipe_data in recipes_data:
            ingredients_data = recipe_data.pop('ingredients')
            recipe, created = Recipe.objects.get_or_create(**recipe_data)
            for ingredient_data in ingredients_data:
                ingredient, created = Ingredient.objects.get_or_create(**ingredient_data)
                recipe.ingredients.add(ingredient)
            restaurant.recipes.add(recipe)
        return restaurant
