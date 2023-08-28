from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ..models import User
from ..views import user_list


class TestUserViews(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_user1 = User.objects.create(username='test_user1', age=25)
        self.test_user2 = User.objects.create(username='test_user2', age=30)

    def test_create_user(self):
        data = {'username': 'new_test_user', 'age': 28}
        request = self.factory.post('/api/users/', data, format='json')
        response = user_list(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)

    def test_get_user(self):
        request = self.factory.get(f'/api/users/{self.test_user1.id}/')
        response = user_list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.context['users'][0].username, self.user1.username)

    def test_delete_user(self):
        request = self.factory.delete(f'/api/users/{self.test_user2.id}/')
        response = user_list(request)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 1)
