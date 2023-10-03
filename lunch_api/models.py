from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ("EMP", "Employee"),
        ("RES", "Restaurant")
    ]

    user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES)


class Menu(models.Model):
    date = models.DateField(auto_now_add=True)
    restaurant = models.OneToOneField(User, on_delete=models.CASCADE)
    votes = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f'Menu. {self.restaurant}'


class Dishes(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=None)
    dish_name = models.CharField(max_length=255, verbose_name='Dish name')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        restaurant = str(self.menu)[6:]  # cut off 'Menu. ' from string
        return f'{self.dish_name} - {restaurant}'


