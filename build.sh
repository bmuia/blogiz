#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python3 manage.py collectstatic --no-input

# Apply database changes
python3 manage.py makemigrations

# Apply any outstanding database migrations
python3 manage.py migrate

# Check if any users exist in the database, if not, run seeding
if ! python3 manage.py shell -c "from users.models import CustomUser; print(CustomUser.objects.exists())" | grep -q "True"; then
  echo "No users found. Seeding users and posts..."
  
  # Seed users
  python3 manage.py seed_users

  # Seed posts
  python3 manage.py seed_posts
else
  echo "Users already exist. Skipping seeding."
fi
