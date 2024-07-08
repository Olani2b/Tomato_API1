from django.contrib import admin
from .models import Restaurant, Recipe, Ingredient

admin.site.register(Restaurant)
admin.site.register(Recipe)
admin.site.register(Ingredient)
