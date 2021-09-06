from rest_framework import serializers

class RecipeItemSerializer(serializers.Serializer):
    step=serializers.IntegerField(min_value=1)
    text=serializers.CharField()