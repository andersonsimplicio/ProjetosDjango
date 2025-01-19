from django.test import TestCase
from django.urls import resolve, reverse

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
            '''
            # Teste authors urls
            '''
            return super().setUp()
    
    def test_authors_registrer_url_is_correct(self):
        url = reverse('apps.authors:register')
        self.assertEqual(url, '/authors/register/')
        