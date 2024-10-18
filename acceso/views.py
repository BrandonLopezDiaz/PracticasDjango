from rest_framework.viewsets import ModelViewSet
from acceso.models import acceso
from acceso.serializers import AccesoSerializer
from acceso.filters import AccesosFilter
from filters.mixins import FiltersMixin
from rest_framework.pagination import LimitOffsetPagination



class AccesoModelViewSet(AccesosFilter,FiltersMixin, ModelViewSet  ):
    queryset = acceso.objects.all()
    serializer_class = AccesoSerializer
    model = acceso
    def get_queryset(self):
        return self.filter_queryset(super().get_queryset())