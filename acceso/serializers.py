from rest_framework.serializers import ModelSerializer
from acceso.models import acceso

class AccesoSerializer(ModelSerializer):
    class Meta:
        model = acceso
        fields = ['id','acceso']