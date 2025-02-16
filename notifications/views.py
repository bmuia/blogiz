from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer

# Admin only can create notifications
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_notification(request):
    """
    Create a new notification. Only accessible by admin.
    """
    if request.method == 'POST':
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Authenticated users can view notifications
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    """
    Get all notifications (for authenticated users).
    """
    notifications = Notification.objects.filter(admin_only=True).order_by('-created_at')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
