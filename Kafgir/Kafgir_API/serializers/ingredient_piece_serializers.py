from rest_framework import serializers

class IngredientPieceSerializer(serializers.Serializer):
    '''This is a serializer for IngredientPieceInput DTO. We use this serializer just to validate our data.'''

    name = serializers.CharField(max_length=255)
    amount = serializers.CharField(max_length=255)
