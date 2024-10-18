from django.test import TestCase
from django.urls import resolve, reverse
#Nunca esquecer de passa caminho absoluto apps...
from apps.receitas.views import home,categoria,receita


class ReceitaViewsTest(TestCase):
    
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('apps.receitas:home'))
        self.assertIs(view.func,home)
        
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('apps.receitas:categoria', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, categoria)
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('apps.receitas:receita', kwargs={'id': 1})
        )
        self.assertIs(view.func,receita)
        
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
        response = self.client.get(
            reverse('apps.receitas:receita', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
   
    '''   
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('apps.receitas:home'))
        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            response.content.decode('utf-8')
        )
    '''  