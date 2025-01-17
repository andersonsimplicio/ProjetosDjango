from django.test import TestCase
from django.urls import resolve, reverse
#Nunca esquecer de passa caminho absoluto apps...
from apps.receitas.views import home,categoria,receita,search
from django.contrib.auth.models import User
from apps.receitas.tests.test_recipe_base import RecipeTestBase
from unittest import skip


class RecipeSearchViewTest(RecipeTestBase):
    
    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('apps.receitas:search'))
        self.assertIs(resolved.func,search)
    
    def test_recipe_search_loads_correct_template(self):
        url = reverse('apps.receitas:search')
        response = self.client.get(url, {'q': 'bolo'})
        self.assertTemplateUsed(response, 'receitas/pages/search.html')
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('apps.receitas:search')
        response = self.client.get(url) 
        '''
        Na falta do termo q de pesquisa haverá um erro  404
        
        '''
        self.assertEqual(response.status_code, 404)
        
    def test_receita_conteudo_ola(self):
        url = reverse('apps.receitas:search')
        response = self.client.get(f'{url}?q=bolo')
        self.assertEqual(response.status_code, 200)
        
    
    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('apps.receitas:search') + '?q=<Teste>'
        response = self.client.get(url)
        
        self.assertIn('Busca por &quot;&lt;Teste&gt;&quot;', response.content.decode('utf-8'))
    
    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'
        recipe1 = self.make_recipe(
            slug='one', title=title1, author_data={'username': 'one'}
        )
        recipe2 = self.make_recipe(
            slug='two', title=title2, author_data={'username': 'two'}
        )
        search_url = reverse('apps.receitas:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        
        response_both = self.client.get(f'{search_url}?q=this')
        
        self.assertIn(recipe1, response1.context['receitas'])
        self.assertNotIn(recipe2, response1.context['receitas'])
        
        self.assertIn(recipe2, response2.context['receitas'])
        self.assertNotIn(recipe1, response2.context['receitas'])
        
        self.assertIn(recipe1, response_both.context['receitas'])
        self.assertIn(recipe2, response_both.context['receitas'])