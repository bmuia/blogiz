from rest_framework import serializers
from posts.serializers import PostSerializer
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
    posts = PostSerializer(many=True, read_only=True) 
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'profile_picture','posts']
