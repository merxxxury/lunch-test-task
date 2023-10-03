from django.contrib import admin
from .models import User, Menu, Dishes


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    pass
