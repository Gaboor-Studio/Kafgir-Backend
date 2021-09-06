from rest_framework import serializers

class TagInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    is_main = serializers.BooleanField()
    is_primary = serializers.BooleanField()
    display_order = serializers.IntegerField()
