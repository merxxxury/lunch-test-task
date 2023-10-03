from rest_framework import serializers
from .models import User, Menu, Dishes
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .utils import CurrentUserDefaultOverridden


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'user_type')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            user_type=validated_data['user_type']
        )

        user.set_password(validated_data['password'])
        user.save()

        # create an instance in the Menu model
        if user.user_type == 'RES':
            restaurant = User.objects.get(pk=user.pk)
            menu_instance = Menu.objects.create(restaurant=restaurant)
            menu_instance.save()

        return user


class DishesSerializer(serializers.ModelSerializer):
    menu = serializers.HiddenField(default=CurrentUserDefaultOverridden())

    class Meta:
        model = Dishes
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
