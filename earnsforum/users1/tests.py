from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserCreationForm, LoginForm, UserProfileUpdateForm
from .models import UserProfile

class FormTest(TestCase):
    def setUp(self):
        self.client = Client()

class UserAccountTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

def test_user_signup(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users1/signup.html')

        # Test valid form submission
        form_data = {'username': 'newuser', 'password1': 'newpassword123', 'password2': 'newpassword123'}
        response = self.client.post(self.signup_url, form_data)
        self.assertEqual(response.status_code, 302)  # Redirect on successful signup
        self.assertTrue(User.objects.filter(username='newuser').exists())


def test_user_login(self):
    # Test login page load
    response = self.client.get(self.login_url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'users1/login.html')
    # Test valid login
    login_data = {'username': 'testuser', 'password': '12345'}
    response = self.client.post(self.login_url, login_data, follow=True)
    self.assertTrue(response.context['user'].is_authenticated)
    # Check redirection after login
    self.assertRedirects(response, 'starting-page')  # Update as per your redirection logic


def test_user_logout(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.logout_url)
        self.assertFalse(response.context['user'].is_authenticated)


def test_profile_update(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)

        # Test valid profile update
        update_data = {'field1': 'value1', 'field2': 'value2'}  # Replace with actual field names and values
        response = self.client.post(self.profile_url, update_data)
        self.assertRedirects(response, 'users1:profile')  # Update as per your redirection logic
        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.field1, 'value1')  # Replace with actual field names