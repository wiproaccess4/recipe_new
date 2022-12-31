from django.urls import path, include
from . import views

urlpatterns = [
    path('info/', views.recipe_info, name="recipe_list"),
    path('create/', views.create_recipe, name="create"),
    path('contact/', views.contact, name="contact"),
]
