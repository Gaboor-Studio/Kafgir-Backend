from rest_framework import serializers

class IngredientPieceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    amount = serializers.CharField(max_length=255)
