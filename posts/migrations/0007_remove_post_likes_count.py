# Generated by Django 5.0.2 on 2024-12-26 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_comments_count_post_likes_count_comment_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes_count',
        ),
    ]
