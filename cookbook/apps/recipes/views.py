from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipe

class RecipeListView(generics.ListCreateAPIView):
    model = Recipe
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        timing = self.request.query_params.get('timing')

        if timing:
            queryset = queryset.filter(timing=timing)
        return queryset

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()