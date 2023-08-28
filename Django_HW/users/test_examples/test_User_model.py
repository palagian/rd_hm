import re
from django.test import TestCase
from ..models import User


class TestUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='test_user', age=25, password='poLzxcq96/')

    def test_age_is_integer(self):
        user = User.objects.get(id=1)
        self.assertIsInstance(user.age, int)

    def test_age_is_nullable(self):
        user = User.objects.get(id=1)
        self.assertIsNone(user.age)

    def test_password_requirements(self):
        user = User.objects.get(id=1)
        password = user.password

        # Define password requirements
        has_minimum_length = len(password) >= 8
        has_uppercase = re.search(r'[A-Z]', password) is not None
        has_digit = re.search(r'\d', password) is not None
        has_special_character = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

        self.assertTrue(has_minimum_length)
        self.assertTrue(has_uppercase)
        self.assertTrue(has_digit)
        self.assertTrue(has_special_character)

    def test_username_not_empty(self):
        user = User.objects.get(id=1)
        self.assertTrue(len(user.username) > 0)
