from rest_framework import serializers

class ShoppingListInputSerializer(serializers.Serializer):
    '''This serializer is used to update shopping list item .'''

    title = serializers.CharField(max_length=255)
    done = serializers.BooleanField()
    amount = serializers.CharField(max_length=255)

class CreateShoppingListInputSerializer(serializers.Serializer):
    '''This serializer is used to create shopping list item .'''

    title = serializers.CharField(max_length=255)
    amount = serializers.CharField(max_length=255)
