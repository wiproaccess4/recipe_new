from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from recipe.models import Recipe

class RecipeApiView(APIView):

    def get(self, request):
        recipes = Recipe.objects.values("id", "name", "ingredients")
        return Response({"message": "success", "data": recipes})

    def put(self, request):
        recipe = Recipe.objects.get(id=request.data.get("id"))
        recipe.name = request.data.get("name")
        recipe.save()
        return Response({"message": "updated Successfully"})
