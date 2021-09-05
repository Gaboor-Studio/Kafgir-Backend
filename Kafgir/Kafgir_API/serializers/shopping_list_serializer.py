from rest_framework import serializers

class ShopingListInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    amount = serializers.CharField(max_length=255)

   