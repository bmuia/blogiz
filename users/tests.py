from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import CustomUser

class UserRegistrationTest(APITestCase):
    def test_register_user(self):
        url = reverse('user_register') 
        data = {
            'email': 'testuser@example.com',
            'password': 'securepassword123',
            'profile_picture': '',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('email', response.data)  #
        self.assertEqual(response.data['email'], 'testuser@example.com')

class UserProfileTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com', password='securepassword123'
        )
        self.client.force_authenticate(user=self.user)  # Authenticate test client

    def test_get_profile(self):
        url = reverse('user_profile')  # URL defined in users/urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # HTTP 200 OK
        self.assertEqual(response.data['email'], self.user.email)


class UserLoginTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com', password='securepassword123'
        )

    def test_login_user(self):
        url = reverse('token_obtain_pair')
        data = {
            'email': 'testuser@example.com',
            'password': 'securepassword123',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)  
        self.assertIn('refresh', response.data) 

