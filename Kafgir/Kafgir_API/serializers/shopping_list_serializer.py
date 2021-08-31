from rest_framework import serializers
from ..models.shopping_list_item import ShoppingListItem

class ShopingListInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    done = serializers.BooleanField()
    amount = serializers.IntegerField()
    unit = serializers.CharField(max_length=255)

    def validate(self, data):
            
         unit = data['unit']
         if unit not in [choice[0] for choice in ShoppingListItem.CHOICES] :
             raise serializers.ValidationError('Invalid choice of unit. must choose between kg, g, Number and Liter!')

         return data