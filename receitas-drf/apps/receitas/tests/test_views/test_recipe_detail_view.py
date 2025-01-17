from django.urls import resolve, reverse
#Nunca esquecer de passa caminho absoluto apps...
from apps.receitas.views import receita
from apps.receitas.tests.test_recipe_base import RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):
    
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
    
    def test_recipe_detail_template_loads_the_corrects_recipes(self):
                
        needed_title = 'This is a detail page - It load one recipe'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('apps.receitas:receita',kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        # Check if one recipe exists
        self.assertIn(needed_title, content)
    
    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        receita = self.make_recipe(is_published=False)
        response = self.client.get(reverse('apps.receitas:receita',kwargs={'id':receita.id}))
        self.assertEqual(response.status_code, 404)