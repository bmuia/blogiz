from rest_framework import serializers
from .models import CustomUser

# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'profile_picture']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

# User Detail Serializer
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'profile_picture']