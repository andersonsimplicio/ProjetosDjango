from django.test import TestCase
from django.urls import resolve, reverse
#Nunca esquecer de passa caminho absoluto apps...
from apps.receitas.views import home,categoria,receita
from django.contrib.auth.models import User
from .test_recipe_base import RecipeTestBase
from unittest import skip

class RecipeViewsTest(RecipeTestBase):
       
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe(category_data={'name':'Bolo com cobertura de Leite Ninho'})
        
        response = self.client.get(reverse('apps.receitas:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['receitas']

        self.assertIn('Bolo com cobertura de Leite Ninho', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)
    
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
        self.assertTemplateUsed(response, 'receitas/partials/header.html')
        self.assertTemplateUsed(response, 'receitas/partials/search.html')
        self.assertTemplateUsed(response, 'receitas/partials/footer.html')
      
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('apps.receitas:categoria', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, categoria)
    
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('apps.receitas:categoria', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('apps.receitas:receita', kwargs={'id': 1})
        )
        self.assertIs(view.func,receita)
    
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        self.make_recipe()
        response = self.client.get(
            reverse('apps.receitas:receita', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)        
        response = self.client.get(reverse('apps.receitas:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['receitas']
        self.assertIn('Bolo de Chocolate', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)
    
    #@skip("Apenas um teste de pulo de teste")        
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        
        response = self.client.get(reverse('apps.receitas:home'))
        self.assertIn(
            '<h1>Não existe receitas 🥲</h1>',
            response.content.decode('utf-8')
        )
    
    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('apps.receitas:categoria', args=(1,)))
        content = response.content.decode('utf-8')
        # Check if one recipe exists
        self.assertIn(needed_title, content)