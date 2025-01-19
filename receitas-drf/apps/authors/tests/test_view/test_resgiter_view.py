from django.test import TestCase
from django.urls import resolve, reverse

class AuthorsTestView(TestCase):
    def setUp(self) -> None:
            '''
            # Teste a view register
            '''
            return super().setUp()
    
    def test_authors_template_loads_register(self):
        response = self.client.get(reverse('apps.authors:register'))

        self.assertIn('<h2>Register</h2>\n',response.content.decode('utf-8'))