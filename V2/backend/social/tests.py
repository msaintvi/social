from django.test import TestCase
from .models import User, Post

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            password="securepassword123",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            date_of_birth="2000-01-01",
            about="Just a test user.",
            avatar="",
            privacy="public"
        )

        self.post = Post.objects.create(
            title="Sample Post",
            content="This is a test post.",
            creator=self.user.username 
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Sample Post")
        self.assertEqual(self.post.creator, "testuser")
