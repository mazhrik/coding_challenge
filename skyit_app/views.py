from django.shortcuts import render
from rest_framework.templatetags.rest_framework import data
from rest_framework.viewsets import ViewSet
# Create your views here.
from rest_framework.response import Response
from rest_framework import status

from skyit_app.models import vechile_model


class vechileViewSet(ViewSet):
    def update_profile(self, request, *args, **kwargs):
        asset_id = kwargs['pk']
        print(asset_id, "--------")
        try:
            asset_id_obj = vechile_model.objects.filter(id=asset_id).values()
        except Exception as error:
            response = {
                'message': error,
            }
            return Response(response)

        if request.data is not None:
            if not asset_id_obj:
                response = {
                    'message': "empty",
                }
                return Response(response)

            else:
                try:
                    mileage = request.data['mileage']
                    # manufacturer = request.data['manufacturer']
                    # status = request.data['status']
                    asset_id_obj.update(mileage=mileage)

                    response = {
                        'message': 'Profile Updated'
                    }

                    return Response(response)
                except Exception as error:

                    response = {
                        'message': 'Error in updating profile',
                        'result': str(error)
                    }
                    return Response(response)

