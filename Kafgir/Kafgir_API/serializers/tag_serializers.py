from rest_framework import serializers

class TagInputSerializer(serializers.Serializer):
    '''This serializer is used to create tag .'''

    title = serializers.CharField(max_length=255)
    is_main = serializers.BooleanField()
    is_primary = serializers.BooleanField()
    display_order = serializers.IntegerField()
    image= serializers.ImageField(required=False)


class TagSetTpSerializer(serializers.Serializer):
    ''' This serializer is used to set tag image.'''
    
    image= serializers.ImageField()
