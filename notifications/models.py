from django.db import models
from django.utils import timezone

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
