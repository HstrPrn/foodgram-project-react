from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.views import IngredientViewSet, TagViewSet, RecipeViewSet


recipes_router = DefaultRouter()
recipes_router.register('tags', TagViewSet)
recipes_router.register('ingredients', IngredientViewSet)
recipes_router.register('recipes', RecipeViewSet)


urlpatterns = [
    path('', include(recipes_router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
