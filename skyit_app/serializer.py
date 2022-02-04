from rest_framework import serializers
from .models import vechile_model
class vehicle_Serializer(serializers.ModelSerializer):

    class Meta:
        model = vechile_model
        fields = '__all__'
