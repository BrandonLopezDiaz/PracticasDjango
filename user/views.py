from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserSerializer
from user.filters import UserFilter
from filters.mixins import FiltersMixin
from rest_framework.pagination import LimitOffsetPagination

class MyCustomPagination(LimitOffsetPagination):
    pass

class UserModelViewSet(UserFilter,FiltersMixin, ModelViewSet  ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User
    pagination_class = MyCustomPagination
    def get_queryset(self):
        return self.filter_queryset(super().get_queryset())