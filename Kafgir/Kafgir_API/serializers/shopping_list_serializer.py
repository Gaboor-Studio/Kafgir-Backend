from rest_framework import serializers

class ShopingListInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    done = serializers.BooleanField()
    amount = serializers.IntegerField()
    unit = serializers.CharField(max_length=255)

   