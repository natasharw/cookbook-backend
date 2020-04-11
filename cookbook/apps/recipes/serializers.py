from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    time_category = serializers.CharField(required=False)
    class Meta:
        model = Recipe
        fields = (
            'pk',
            'name',
            'created_at',
            'time_category',
            'recipe_detail',
            )