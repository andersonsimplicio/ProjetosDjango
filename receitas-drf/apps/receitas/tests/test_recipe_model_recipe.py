from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from .test_recipe_base import Receita, RecipeTestBase
import uuid

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    
    def make_recipe_no_defaults(self):
        recipe = Receita(
            category=self.make_category(name='Test Default Category'),
            author=self.make_author(username='newuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug=f'recipe-{uuid.uuid4().hex[:8]}',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=False
        )
        recipe.full_clean()
        recipe.save()
        return recipe
    
        
    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
         
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
    
    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.preparation_steps_is_html,msg='Receita preparation_steps_is_html não é falso',)
        
    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.is_published, msg='Receita is_publish não é falsa!',)
        
    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), needed,
            msg=f'Receita string representação deve ser '
                f'"{needed}" mas "{str(self.recipe)}" não são iguais.'
        )        