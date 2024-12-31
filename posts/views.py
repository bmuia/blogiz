from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from .models import Post, Like, Comment
from .serializers import PostSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Like Post
@api_view(['POST'])
def like_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user  # Assuming the user is authenticated

    # Check if the user has already liked the post
    if Like.objects.filter(post=post, user=user).exists():
        return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a like
    Like.objects.create(post=post, user=user)

    # Increment the likes_count
    post.likes_count += 1
    post.save()

    return Response(PostSerializer(post).data)



# Post Views
class PostCreateApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)

class PostApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserPostsApi(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        This will return the posts of a specific user by user_id.
        """
    def get_queryset(self):
        """
        This will return the posts of the currently authenticated user.
        """
        user = self.request.user  # Get the authenticated user

        # Return posts filtered by the current user
        return Post.objects.filter(author=user)

class PostDetailApi(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

class PostUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
