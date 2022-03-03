import json

from django.shortcuts import render
from django.utils import timezone
# from django.utils.datetime_safe import datetime
from django.utils.datetime_safe import datetime
from rest_framework.templatetags.rest_framework import data
from rest_framework.viewsets import ViewSet
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
import datetime
from skyapp.models import vechile_m, date_vehicle
from rest_framework.renderers import JSONRenderer

from skyapp.serializers import date_Serializer


class vechileViewSet(ViewSet):


    def update_profile(self, request, *args, **kwargs):
        """
           This function will update only mileage
           but we need to provide it number_plate of the car .It takes number plate no as parameter in the url.
           It searches for the number plate
           of that specific car and then update its mileage according to
           whatever value you give to  .
          """

        asset_id = kwargs['pk']
        print(asset_id, "--------")
        try:
            asset_id_obj = vechile_m.objects.filter(number_plate_number=asset_id).values()
        except Exception as error:
            response = {
                'message': error,
            }
            return Response(response)

        if request.data is not None:
            if not asset_id_obj:
                response = {
                    'message': "not found",
                }
                return Response(response)

            else:
                try:
                    """
                    this part of  function adds the updated mileage  ,number_plate and time on which mileage was 
                    updated to a another table i.e date_vehicle
                    """
                    mileage = request.data['mileage']
                    asset_id_obj.update(mileage=mileage)
                    # x = datetime.now()
                    # print("------", type(x))
                    response = {
                        'message': 'Profile Updated'
                    }

                    vechile_date = date_vehicle(number_plate_number=asset_id, date=datetime.datetime.now(), mileage=mileage)
                    vechile_date.save()

                    return Response(response)
                except Exception as error:

                    response = {
                        'message': 'Error in updating profile',
                        'result': str(error)
                    }
                    return Response(response)

    def finding_mileage(self, request, *args, **kwargs):
        """
        we give date and number plate of a car as url params
        to find  the value of the mileage the  car has since the given date
        to current date

        """
        date = kwargs['date']

        date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        number_plate_of_car = kwargs['number_plate_of_car']
        print('----------->', datetime.datetime.now())
        try:
            if all(v is not None for v in [number_plate_of_car, date]):
                obj = date_vehicle.objects.filter(number_plate_number=number_plate_of_car,
                                                  date__range=[date, datetime.datetime.now()]).order_by('id').all()
                data_serializer = date_Serializer(obj, many=True)
                json_data = JSONRenderer().render(data_serializer.data)
                json_date_vehicle = json.loads(json_data)

                x = 1
                y = len(json_date_vehicle)
                for i in json_date_vehicle:
                    if x == 1:

                        mileage_date = i['mileage']
                    elif x == y:

                        mileage_date2 = i['mileage']
                    x += 1

                final_mileage = int(mileage_date2) - int(mileage_date)


            else:
                pass
        except Exception as error:
            response = {
                'message': str(error)
            }
            return Response(response)
        response = {
            'Total mileage': final_mileage
        }
        return Response(response)


from django.shortcuts import render
