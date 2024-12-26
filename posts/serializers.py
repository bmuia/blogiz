from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_email = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__' 
        read_only_fields = ['author']

    def get_author_email(self, obj):
        return obj.author.email if obj.author else None
