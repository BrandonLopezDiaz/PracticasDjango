from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.Serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from posts.api.permissions import IsAdminOrReadOnly
from posts.api.filters import PostsFilter
#Usando de esta manera la clase sirve para crear un crud completo
#De igual forma sirve para autentificacion y permisos del usuario
class PostModelViewSet(ModelViewSet, PostsFilter ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    model = Post
    # permission_classes = [IsAdminOrReadOnly]
    #en esta linea le podemos decir que solo queremos esos metodos del crud
    #http_method_names = ['get','put', 'delete', 'patch']




# class PostViewSet(ViewSet):
#     def list(self, request):
#         # posts = Post.objects.all()
#         # posts = [post.title for post in Post.objects.all()]
#         serializer = PostSerializer(Post.objects.all(), many= True)
#         print(f"hola {request}")
#         return Response(status= status.HTTP_200_OK, data=serializer.data)
    
#     def retrieve(self, request, pk: int):
#         try:
#             post = PostSerializer(Post.objects.get(pk = pk ))
#             return Response(status=status.HTTP_200_OK, data=post.data)
#         except Exception as c:
#             return Response(status=status.HTTP_400_BAD_REQUEST , data= f'Hubo un error del tipo {c}')

#     def create(self, request):
#         # Post.objects.csreate(title=request.POST['title'], description=request.POST['description'], 
#         #                     order=request.POST['order'])
#         # return self.get(request)
#         seralizer = PostSerializer(data= request.POST)
#         seralizer.is_valid(raise_exception= True)
#         seralizer.save()
#         return Response(status=status.HTTP_200_OK, data=seralizer.data)
    


# class PostApiView(APIView):
#     def get(self, request):
#         # posts = Post.objects.all()
#         # posts = [post.title for post in Post.objects.all()]
#         serializer = PostSerializer(Post.objects.all(), many= True)
#         return Response(status= status.HTTP_200_OK, data=serializer)
    
#     def post(self, request):
#         # Post.objects.create(title=request.POST['title'], description=request.POST['description'], 
#         #                     order=request.POST['order'])
#         # return self.get(request)
#         seralizer = PostSerializer(data= request.POST)
#         seralizer.is_valid(raise_exception= True)
#         seralizer.save()
#         return Response(status=status.HTTP_200_OK, data=seralizer.data)
