from rest_framework import serializers

class FoodPlanInputSerializer(serializers.Serializer):
    date_time = serializers.CharField(max_length=255)
    breakfast = serializers.IntegerField()
    lunch = serializers.IntegerField()
    dinner = serializers.IntegerField()
