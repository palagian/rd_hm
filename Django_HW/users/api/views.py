from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from users.api.filters import UserFilter
from users.api.pagination import CustomPagination
from users.api.serializers import UserSerializer
from users.models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    pagination_class = CustomPagination


    @action(methods=['GET'], detail=False)
    def no_email(self, request):
        qs = self.get_queryset().filter(email='')
        serializer = self.get_serializer(qs, many=True)
        from rest_framework.response import Response
        return Response(serializer.data)
