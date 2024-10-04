from rest_framework.viewsets import ModelViewSet
from filters.mixins import FiltersMixin
from rest_framework.pagination import LimitOffsetPagination
from temario.models import Temas, SubTemas
from temario.serializers import TemasSerializer, SubTemasSerializer
from temario.filters import TemasFilter


class MyCustomPagination(LimitOffsetPagination):
    pass
class TemasModelViewSet(TemasFilter,FiltersMixin, ModelViewSet  ):
    queryset = Temas.objects.all()
    serializer_class = TemasSerializer
    model = Temas
    pagination_class = MyCustomPagination
    def get_queryset(self):
        return self.filter_queryset(super().get_queryset())

class SubTemasModelViewSet(TemasFilter,FiltersMixin, ModelViewSet  ):
    queryset = SubTemas.objects.all()
    serializer_class = SubTemasSerializer
    model = SubTemas
    pagination_class = MyCustomPagination
    def get_queryset(self):
        return self.filter_queryset(super().get_queryset())