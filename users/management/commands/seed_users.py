# users/management/commands/seed_users.py

from django.core.management.base import BaseCommand
from users.models import CustomUser
from faker import Faker

class Command(BaseCommand):
    help = 'Generates fake users in the database'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Number of users you want to create
        num_users = 50
        
        for _ in range(num_users):
            user = CustomUser.objects.create_user(
                email=fake.email(),
                password=fake.password(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                profile_picture=fake.image_url()  # Random image URL for the profile
            )
            
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {num_users} users'))
