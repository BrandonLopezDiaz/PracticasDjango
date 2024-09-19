from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'description', 'orden', 'created_at']
        #Otro modo que trae a todo del modelo
        # fields = '___all__'