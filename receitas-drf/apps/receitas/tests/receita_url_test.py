from django.test import TestCase
from django.urls import reverse

class RecipeURLsTest(TestCase):
    
    def test_recipe_home_url_is_correct(self):
        url = reverse('apps.receitas:home')
        self.assertEqual(url, '/')
        
    def test_recipe_categoria_url_is_correct(self):
        url = reverse('apps.receitas:categoria', kwargs={'category_id': 1})
        self.assertEqual(url, '/receitas/categoria/1/')
        
    def test_receita_detail_url_is_correct(self):
        url = reverse('apps.receitas:receita', kwargs={'id': 1})
        self.assertEqual(url, '/receita/1/')