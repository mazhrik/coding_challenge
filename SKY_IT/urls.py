"""SKY_IT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include

import skyapp2
from skyapp2.views import car_class

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skyit_url/', include('skyapp.urls')),
    path('disp/', include('skyapp2.urls')),
    path('delete/<str:color>', skyapp2.views.Destroy_api.as_view()),
    path('list/', skyapp2.views.car_class.as_view()),
    path('create/', skyapp2.views.create_car.as_view()),
    path('update/<int:id>', skyapp2.views.Update_car.as_view())
]
