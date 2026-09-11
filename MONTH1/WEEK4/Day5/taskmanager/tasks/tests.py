from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Task,Project


User=get_user_model()
class TaskTest(TestCase):
    def test_something(self):
        self.assertEqual(1+1,2)

    def setUp(self):
        self.user=User.objects.create_user(
            username="huzaifa",
            password="Test123"

        )
        self.project=Project.objects.create(
            title="Django Project",
            owner=self.user
        )