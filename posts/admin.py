# posts/admin.py
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image_url', 'image', 'created_at', 'updated_at')  # Add fields to display in the list view
    search_fields = ('title', 'content')  # Add search functionality by title and content

admin.site.register(Post, PostAdmin)
