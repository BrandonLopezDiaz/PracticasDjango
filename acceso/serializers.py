from rest_framework.serializers import ModelSerializer
from acceso.models import acceso
from user.serializers import UserSerializer

class AccesoSerializer(ModelSerializer):
    acceso_list = UserSerializer(many= True, read_only=True)
    class Meta:
        model = acceso
        fields = ['id','acceso', 'acceso_list']