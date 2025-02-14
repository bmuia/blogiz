from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Getting the User model
User = get_user_model()

# Custom image validator function
def validate_image_extension(value):
    if not value.name.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValidationError("Only .jpg, .jpeg, or .png image formats are allowed.")

class Image(models.Model):
    key = models.CharField(help_text="The public id of the uploaded file", max_length=100)
    url = models.URLField()
    name = models.CharField(max_length=100, help_text='The original name of the uploaded image')
    width = models.IntegerField(help_text='Width in pixels')
    height = models.IntegerField(help_text='Height in pixels')
    format = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    content = models.TextField()
    image = models.OneToOneField(Image, on_delete=models.SET_NULL, null=True, blank=True)  # Fixed reference to Image model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def likes_count(self):
        return self.likes.count()

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.first_name} on {self.post.title}'
