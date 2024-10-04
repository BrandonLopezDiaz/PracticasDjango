from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.apps import apps
from temario.models import Temas, SubTemas

class TemasGenericSerializer(ModelSerializer):
    # Temas = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Temas
        fields = ['id','titulo', 'descripcion', 'video_url', 'imagen_url',]

class TemasSerializer(TemasGenericSerializer):
    subtemas_relacion = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Temas
        fields = ['id','titulo', 'descripcion', 'video_url', 'imagen_url','subtemas_relacion']

class SubTemasSerializer(TemasGenericSerializer):
    # Temas = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = SubTemas
        fields = ['id','titulo', 'descripcion', 'video_url', 'imagen_url','tema']