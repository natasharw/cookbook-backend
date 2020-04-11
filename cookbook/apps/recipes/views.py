from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipe

class RecipeListView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()