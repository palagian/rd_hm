import django_filters

from users.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'age': ['exact', 'gte', 'lte'],
            'username': ['icontains'],
        }