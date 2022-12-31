from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.RecipeApiView.as_view(), name="recipe_api"),
]
