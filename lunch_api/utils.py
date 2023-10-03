from rest_framework.fields import CurrentUserDefault

from .models import Menu


# to fix error with LazyQuery
class CurrentUserDefaultOverridden(CurrentUserDefault):

    def __call__(self, serializer_field):
        user = serializer_field.context['request'].user
        return Menu.objects.get(pk=user.pk)
