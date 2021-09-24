from rest_framework import serializers

class CreateCommentSerializer(serializers.Serializer):
    '''This serializer is used to create comment .'''

    rating = serializers.IntegerField(min_value=0,max_value=10)
    text = serializers.CharField()

class UpdateCommentSerializer(serializers.Serializer):
    '''This serializer is used to update comment .'''

    rating = serializers.IntegerField(min_value=0,max_value=10)
    text = serializers.CharField()

class CommentIdListSerializer(serializers.Serializer):
    '''This serializer receives a list of comment IDs for administrator to confirm user comments .'''

    commentid_list = serializers.ListField(child = serializers.IntegerField())
