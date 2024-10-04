from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from user.models import User
from acceso.models import acceso

class UserSerializer(ModelSerializer):
    accesos = serializers.SlugRelatedField(queryset= acceso.objects.all(), slug_field='acceso', many=True)
    # accesos = serializers.PrimaryKeyRelatedField(queryset=acceso.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'nombre','apellido','direccion','email','password','created_at','accesos',]
