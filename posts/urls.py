from django.urls import path
from .views import PostCreateApi, PostApi,PostUpdateApi,PostDeleteApi
urlpatterns = [
    path('posts', PostApi.as_view()),
    path('posts/create',PostCreateApi.as_view()),
    path('posts/update/<int:pk>',PostUpdateApi.as_view()),
    path('posts/delete/<int:pk>',PostDeleteApi.as_view())
]