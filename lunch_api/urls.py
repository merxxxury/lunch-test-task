from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *


router = routers.DefaultRouter()


urlpatterns = [

    path('register/', RegisterView.as_view(), name='auth_register'),
    path('api_auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('dishes', DishesAPIList.as_view(), name='dishes'),
    path('menus', MenuAPIList.as_view(), name='menu'),
]
