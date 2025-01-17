from django.urls import resolve, reverse
#Nunca esquecer de passa caminho absoluto apps...
from apps.receitas.views import categoria
from apps.receitas.tests.test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):
    
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
        
    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('apps.receitas:categoria', args=(1,)))
        content = response.content.decode('utf-8')
        # Check if one recipe exists
        self.assertIn(needed_title, content)
    
    def test_recipe_category_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        receita = self.make_recipe(is_published=False)
        response = self.client.get(reverse('apps.receitas:categoria',kwargs={'category_id':receita.category.id}))
        # Check if one recipe exists
        self.assertEquals(response.status_code,404)