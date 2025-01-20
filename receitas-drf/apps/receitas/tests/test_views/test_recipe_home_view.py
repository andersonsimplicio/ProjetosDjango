from django.urls import resolve, reverse
#Nunca esquecer de passa caminho absoluto apps...
from apps.receitas.views import home
from django.contrib.auth.models import User
from apps.receitas.tests.test_recipe_base import RecipeTestBase
from unittest import skip #utilizado para pular um teste
from unittest.mock import patch

class RecipeHomeViewTest(RecipeTestBase):
    
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('apps.receitas:home'))
        self.assertIs(view.func,home)
    
    def test_recipe_home_view_returns_status_code_200_OK(self):
       response = self.client.get(reverse('apps.receitas:home'))
       self.assertEqual(response.status_code, 200)
    
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('apps.receitas:home'))        
        self.assertTemplateUsed(response, 'receitas/pages/home.html')
        self.assertTemplateUsed(response, 'global/base.html')
        self.assertTemplateUsed(response, 'global/partials/header.html')
        self.assertTemplateUsed(response, 'global/partials/search.html')
        self.assertTemplateUsed(response, 'global/partials/footer.html')
    
    #@skip("Apenas um teste de pulo de teste")        
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        
        response = self.client.get(reverse('apps.receitas:home'))
        self.assertIn(
            '<h1>Não existe receitas 🥲</h1>',
            response.content.decode('utf-8')
        )
    
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe(category_data={'name':'Bolo com cobertura de Leite Ninho'})
        
        response = self.client.get(reverse('apps.receitas:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['receitas']

        self.assertIn('Bolo com cobertura de Leite Ninho', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)
    
    def test_recipe_home_template_dont_load_recipes_not_published(self):
            """Test recipe is_published False dont show"""
            # Need a recipe for this test
            self.make_recipe(is_published=False)
            response = self.client.get(reverse('apps.receitas:home'))
            # Check if one recipe exists
            self.assertIn('<h1>Não existe receitas 🥲</h1>', response.content.decode('utf-8'))
    
    def test_recipe_home_is_paginated(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)
            
        with patch('apps.receitas.views.PER_PAGE', new=3):
            response = self.client.get(reverse('apps.receitas:home'))
            recipes = response.context['receitas']
            paginator = recipes.paginator
            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)
    
    def test_invalid_page_query_uses_page_one(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)
        with patch('apps.receitas.views.PER_PAGE', new=3):
            response = self.client.get(reverse('apps.receitas:home') + '?page=12A')
            self.assertEqual(
                response.context['receitas'].number,
                1
            )
            response = self.client.get(reverse('apps.receitas:home') + '?page=2')
            self.assertEqual(
                response.context['receitas'].number,
                2
            )
            response = self.client.get(reverse('apps.receitas:home') + '?page=3')
            self.assertEqual(
                response.context['receitas'].number,
                3
            )