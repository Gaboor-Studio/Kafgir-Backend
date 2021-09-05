from rest_framework import serializers

from .ingredient_piece_serializer import IngredientPieceSerializer
from .recipe_item_serializer import RecipeItemSerializer

class FoodSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    level = serializers.IntegerField(min_value=1,max_value=3)
    cooking_time = serializers.IntegerField(min_value=1)
    ingredien_pieces = IngredientPieceSerializer(many=True)
    recipte_items = RecipeItemSerializer(many=True)
