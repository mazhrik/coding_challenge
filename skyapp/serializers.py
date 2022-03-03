from rest_framework import serializers
from .models import vechile_m, date_vehicle


class vehicle_Serializer(serializers.ModelSerializer):
    class Meta:
        model = vechile_m
        fields = '__all__'


class date_Serializer(serializers.ModelSerializer):
    class Meta:
        model = date_vehicle
        fields = '__all__'

