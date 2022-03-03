from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import car
from .serializer import car_serializer, cart_serializer
from rest_framework.viewsets import ViewSet


class car_class(ListAPIView):
    queryset = car.objects.all()
    serializer_class = car_serializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("id",)


class Destroy_api(DestroyAPIView):
    queryset = car.objects.all()
    lookup_field = ("color")


class create_car(CreateAPIView):
    queryset = car.objects.all()
    serializer_class = car_serializer

    def create(self, request, *args, **kwargs):
        color = request.data.get('color')
        if color == "red":
            raise ValidationError({'color ': "not allowed"})
        return super().create(request, *args, **kwargs)


class Update_car(RetrieveUpdateDestroyAPIView):
    queryset = car.objects.all()
    serializer_class = car_serializer
    lookup_field = "id"

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class cart_class(ViewSet):

    def disp(self, request):
        try:
            all_car = car.objects.filter(name="ford mustang2")
            serialzier = cart_serializer(all_car, many=True)
        except Exception as e:
            response = {
                "msg": e

            }
            return Response(response)
        import json
        response = {
            "msg": serialzier.data

        }
        return Response(response)
