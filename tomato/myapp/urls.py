from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, RecipeViewSet, IngredientViewSet, home

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('', home, name='home'),          # Home view for the root URL
    path('', include(router.urls)),       # API endpoints
]
