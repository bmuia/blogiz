from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_email = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()  # Adding likes_count field

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']

    def get_author_email(self, obj):
        return obj.author.email if obj.author else None

    def get_likes_count(self, obj):
        # Assuming a ManyToMany relationship with the Like model
        return obj.likes.count()  # Count the number of likes for this post
