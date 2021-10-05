from rest_framework import serializers

class CreateFoodPlanInputSerializer(serializers.Serializer):
    '''This serializer is used to create food plan .'''

    date_time = serializers.DateTimeField()
    breakfast = serializers.IntegerField()
    lunch = serializers.IntegerField()
    dinner = serializers.IntegerField()

class FoodPlanInputSerializer(serializers.Serializer):
    '''This serializer is used to update food plan .'''

    breakfast = serializers.IntegerField()
    lunch = serializers.IntegerField()
    dinner = serializers.IntegerField()
