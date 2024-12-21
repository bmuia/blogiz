from django.urls import path
from .views import PostCreateApi, PostApi,PostUpdateApi,PostDeleteApi
urlpatterns = [
    path('posts', PostApi.as_view(), name='post_list'),
    path('posts/create',PostCreateApi.as_view(),name='post_create'),
    path('posts/update/<int:pk>',PostUpdateApi.as_view(),name='post_update'),
    path('posts/delete/<int:pk>',PostDeleteApi.as_view(),name='post_delete')
]