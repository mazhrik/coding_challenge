from django.urls import path
from skyit_app import views

urlpatterns = [
    path('update_profile/<int:pk>', views.vechileViewSet.as_view({'post': 'update_profile'}), name='update_profile'),
    # path('add_account/', views.Avatar.as_view({'post': 'add_account'}), name='add_account'),

]
