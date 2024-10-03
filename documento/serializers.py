from rest_framework.serializers import ModelSerializer
from documento.models import Documento

class SerializerDocumento (ModelSerializer) :
    class Meta:
        model = Documento
        fields = ['id','videos', 'pdf', 'descripcion',]