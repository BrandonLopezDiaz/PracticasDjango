from rest_framework.viewsets import ModelViewSet
from acceso.models import acceso
from acceso.serializers import AccesoSerializer
from acceso.filters import AccesosFilter
from filters.mixins import FiltersMixin
from rest_framework.pagination import LimitOffsetPagination

class MyCustomPagination(LimitOffsetPagination):
    pass

class AccesoModelViewSet(AccesosFilter,FiltersMixin, ModelViewSet  ):
    serializer_class = AccesoSerializer
    queryset = acceso.objects.all()
    model = acceso
    pagination_class = MyCustomPagination
    def get_queryset(self):
        return self.filter_queryset(super().get_queryset())