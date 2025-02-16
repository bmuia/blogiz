from django.urls import path
from . import views

urlpatterns = [
    path('api/notifications/', views.get_notifications, name='get_notifications'),
    path('api/notifications/create/', views.create_notification, name='create_notification'),
]
