from rest_framework.routers import DefaultRouter
from acceso.views import AccesoModelViewSet

router_acceso = DefaultRouter()
router_acceso.register(r'accesos', basename='acceso', viewset=AccesoModelViewSet)
