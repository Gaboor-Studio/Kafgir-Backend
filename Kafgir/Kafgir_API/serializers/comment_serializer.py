from rest_framework import serializers

class CreateCommentSerializer(serializers.Serializer):
    rating = serializers.IntegerField(min_value=0,max_value=10)
    food = serializers.IntegerField()
    text = serializers.CharField()

class UpdateCommentSerializer(serializers.Serializer):
    rating = serializers.IntegerField(min_value=0,max_value=10)
    text = serializers.CharField()

class CommentIdListSerializer(serializers.Serializer):
    commentid_list = serializers.ListField(child = serializers.IntegerField())
