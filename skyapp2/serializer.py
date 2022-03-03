from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from skyapp2.models import car, shopping_cart


class car_serializer(ModelSerializer):
    class Meta:
        model = car
        fields = "__all__"


class cart_serializer(ModelSerializer):
    car_serilize = serializers.SerializerMethodField()

    class Meta:
        model = shopping_cart
        fields = ('shopping_number', 'car_serilize')

    def get_car_serilize(self, instance):
        shopped_items = car.objects.filter(name=instance)
        return (car_serializer(shopped_items, many=True)).data
