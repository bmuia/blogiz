# posts/management/commands/seed_posts.py

from django.core.management.base import BaseCommand
from posts.models import Post, Like
from users.models import CustomUser
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generates fake posts in the database along with likes'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Number of posts you want to create
        num_posts = 100

        users = CustomUser.objects.all()
        
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create users first.'))
            return
        
        for _ in range(num_posts):
            user = fake.random_element(users)
            post = Post.objects.create(
                title=fake.sentence(),
                author=user,
                content=fake.paragraph(),
                image_url=fake.image_url(),  # Random image URL for the post
            )

            # Ensure num_likes doesn't exceed the number of available users
            num_likes = random.randint(0, min(100, len(users)))  
            liked_users = random.sample(list(users), num_likes) 

            for liked_user in liked_users:
                Like.objects.get_or_create(post=post, user=liked_user)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {num_posts} posts with likes'))
