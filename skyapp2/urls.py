from django.urls import path
from skyapp2 import views
from skyapp2.views import cart_class

urlpatterns = [
    path('disp/', views.cart_class.as_view({'get': 'disp'}), name='disp'),

]
