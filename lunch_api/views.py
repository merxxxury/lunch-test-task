
import datetime

from rest_framework.permissions import AllowAny

from .models import User, Menu, Dishes

from rest_framework import generics
from .serializers import DishesSerializer, MenuSerializer
from .serializers import RegisterSerializer
from .permissions import IsRestaurant
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class DishesAPIList(generics.ListCreateAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    permission_classes = (IsRestaurant, IsAuthenticated)


class MenuAPIList(generics.ListAPIView):
    today_date = datetime.date.today()
    queryset = Menu.objects.filter(date=today_date)
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)
