from rest_framework import serializers
from .models import Recipe, Timing

class TimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timing
        fields = (
            'pk',
            'title'
            )

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'pk',
            'name',
            'owner',
            'timing',
            'detail'
            )
