from rest_framework import generics
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

class PostCreateApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)

class PostApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

