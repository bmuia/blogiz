from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    username = None  # Remove username field
    email = models.EmailField(unique=True)  # Email as unique identifier
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    USERNAME_FIELD = 'email'  # Use email instead of username
    REQUIRED_FIELDS = []  # No extra fields required for superuser creation

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Password Reset Signal Receiver
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Update the reset URL to point to the frontend app
    frontend_url = "https://blogiz-fefab.web.app//reset-password/"
    reset_url = f"{frontend_url}{reset_password_token.key}"
    
    # Email message
    email_plaintext_message = (
        f"Click the link to reset your password: {reset_url}\n"
        "If you did not request this, please ignore this email."
    )

    # Send password reset email
    send_mail(
        subject=f"Password Reset",
        message=email_plaintext_message,
        from_email="no-reply@blogspace.com",
        recipient_list=[reset_password_token.user.email],
        fail_silently=False,
    )
