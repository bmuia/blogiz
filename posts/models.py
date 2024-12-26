from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Getting the User model
User = get_user_model()

# Custom image validator function
def validate_image_extension(value):

    if not value.name.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValidationError("Only .jpg, .jpeg, or .png image formats are allowed.")

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts_images/', validators=[validate_image_extension], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  #

    def __str__(self):
        return self.title
