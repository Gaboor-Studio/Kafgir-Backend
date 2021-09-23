from rest_framework import serializers

class RecipeItemSerializer(serializers.Serializer):
    '''This is a serializer for RecipeItemInput DTO. We use this serializer just to validate our data.'''

    step=serializers.IntegerField(min_value=1)
    text=serializers.CharField()