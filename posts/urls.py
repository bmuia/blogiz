from django.urls import path
from .views import PostCreateApi, PostApi,PostUpdateApi,PostDeleteApi, PostDetailApi,like_post, UserPostsApi

urlpatterns = [
    path('posts/', PostApi.as_view(), name='post_list'),
    path('posts/<int:id>/', PostDetailApi.as_view(), name='post-detail'),
    path('posts/user/', UserPostsApi.as_view(), name='user_posts'),  # Simplified URL
    path('posts/create/', PostCreateApi.as_view(), name='post_create'),
    path('posts/update/<int:pk>/', PostUpdateApi.as_view(), name='post_update'),
    path('posts/delete/<int:pk>/', PostDeleteApi.as_view(), name='post_delete'),
    path('posts/<int:post_id>/like/', like_post, name='like_post'),
]

