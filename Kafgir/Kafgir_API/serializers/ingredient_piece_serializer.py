from rest_framework import serializers

class IngredientPieceSerializer(serializers.Serializer):
    ingredient_name = serializers.CharField(max_length=255),
    amount = serializers.CharField(max_length=255)
