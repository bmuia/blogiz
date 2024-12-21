from rest_framework.test import APITestCase
from django.urls import reverse
from posts.models import Post
from users.models import CustomUser

class PostCreateTest(APITestCase):
    def setUp(self):
        # Create a test user and authenticate
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com', password='securepassword123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        url = '/api/posts/create'  # Endpoint for post creation
        data = {
            'title': 'Test Post',
            'content': 'This is a test post.',
            'author': self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)  # HTTP 201 Created
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, 'Test Post')

class PostListTest(APITestCase):
    def setUp(self):
        # Create a test user and authenticate
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com', password='securepassword123'
        )
        self.client.force_authenticate(user=self.user)  

    def test_get_all_posts(self):
        url = reverse('post_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)






class PostDeleteTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com', password='securepassword123'
        )
        self.post = Post.objects.create(
            title='Test Post', content='Test Content', author=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_delete_post(self):
        url = f'/api/posts/delete/{self.post.id}'  # Delete endpoint
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)  # HTTP 204 No Content
        self.assertEqual(Post.objects.count(), 0)  # Ensure post is deleted
