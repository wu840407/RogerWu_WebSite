from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='測試分類', slug='test-category')
        self.post = Post.objects.create(
            title='測試文章',
            slug='test-post',
            author=self.user,
            content='這是一篇測試文章。',
            category=self.category,
            published=True
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, '測試文章')
        self.assertTrue(self.post.published)
