from django.urls import path
from skyapp import views

urlpatterns = [
    path('update_profile/<int:pk>', views.vechileViewSet.as_view({'post': 'update_profile'}), name='update_profile'),
    path('finding_mileage/<str:date>/<int:number_plate_of_car>',
         views.vechileViewSet.as_view({'post': 'finding_mileage'}),
         name='finding_mileage'),

]
