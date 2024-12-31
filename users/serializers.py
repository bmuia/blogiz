from rest_framework import serializers
from posts.serializers import PostSerializer
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings

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


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        """Check if the email exists in the database."""
        try:
            self.user = get_user_model().objects.get(email=value)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("No user is associated with this email.")
        return value

    def save(self):
        """Send password reset email with token."""
        token = default_token_generator.make_token(self.user)
        reset_link = f"{settings.FRONTEND_URL}/reset-password/{self.user.email}/{token}/"

        # Send email
        send_mail(
            "Password Reset Request",
            f"Click the link to reset your password: {reset_link}",
            settings.DEFAULT_FROM_EMAIL,
            [self.user.email],
            fail_silently=False,
        )
