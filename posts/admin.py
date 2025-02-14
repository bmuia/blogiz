# posts/admin.py
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_image_url', 'image', 'created_at', 'updated_at')
    search_fields = ('title', 'content')

    # Custom method to get image_url in the admin list view
    def get_image_url(self, obj):
        return obj.image_url
    get_image_url.short_description = 'Image URL'  # Optionally change the column name in admin

admin.site.register(Post, PostAdmin)
