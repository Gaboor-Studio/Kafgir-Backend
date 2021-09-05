from rest_framework import serializers

class FoodSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    level = serializers.IntegerField(min=1,max=3)
    cooking_time = serializers.IntegerField(min=1)
    
    ingredient_pieces = serializers.ListField(
        ingredient_name=serializers.CharField(max_length=255),
        amount=serializers.CharField(max_length=255) 
    )

    recipe = serializers.ListField(
        step=serializers.IntegerField(min=1),
        text=serializers.CharField() 
    )

    
