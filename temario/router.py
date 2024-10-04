from rest_framework.routers import DefaultRouter
from temario.views import TemasModelViewSet, SubTemasModelViewSet

router_temario = DefaultRouter()
router_temario.register(r'temas', basename='tema', viewset=TemasModelViewSet)
router_temario.register(r'subtemas', basename='subtema', viewset=SubTemasModelViewSet)