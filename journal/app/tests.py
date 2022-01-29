from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from app.models import User


class AddUserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_data = {
            'username': 'test',
            'name': 'test',
            'email': 'test@local.com'
        }

    def test_add_user(self):
        response = self.client.post(
            '/users/create/',
            data=self.user_data
        )
        self.assertEqual(302, response.status_code)

        new_user = User.objects.get(
            username=self.user_data['username']
        )

        get_str = f'/users/{new_user.pk}/'
        response = self.client.get(get_str)
        self.assertEqual(response.context['user'].email, self.user_data['email'])

    def tearDown(self):
        User.objects.all().delete()