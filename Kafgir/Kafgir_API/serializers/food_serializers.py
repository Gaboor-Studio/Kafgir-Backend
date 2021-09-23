from rest_framework import serializers

from .ingredient_piece_serializers import IngredientPieceSerializer
from .recipe_item_serializers import RecipeItemSerializer

class FoodSerializer(serializers.Serializer):
    '''This is a serializer for FoodInput DTO. We use this serializer just to validate our data.'''

    title = serializers.CharField(max_length=255)
    level = serializers.IntegerField(min_value=1,max_value=3)
    cooking_time = serializers.CharField(max_length=32)
    ingredients = IngredientPieceSerializer(many=True)
    recipe = RecipeItemSerializer(many=True)
    tags = serializers.ListField(child = serializers.IntegerField())
