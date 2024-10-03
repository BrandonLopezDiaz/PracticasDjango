from rest_framework.routers import DefaultRouter
from documento.views import DocumentoModelViewSet

router_documento = DefaultRouter()
# router_post.register(prefix='posts', basename='posts', viewset=PostViewSet)
router_documento.register(r'documentos', basename='documento', viewset=DocumentoModelViewSet)
