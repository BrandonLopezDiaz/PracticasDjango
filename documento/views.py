from rest_framework.viewsets import ModelViewSet
from documento.serializers import SerializerDocumento
from documento.models import Documento
# Create your views here.
class DocumentoModelViewSet(ModelViewSet, SerializerDocumento ):
    serializer_class = SerializerDocumento
    queryset = Documento.objects.all()
    model = Documento
