from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'email']
        read_only_fields = ('id',)
