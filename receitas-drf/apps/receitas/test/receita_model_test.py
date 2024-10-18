from django.test import TestCase

#Nunca esquecer de passa caminho absoluto apps...
from apps.receitas.models import Categoria, Receita, User

class ReceitaModelTest(TestCase):
    
    def test_recipe_home_template_loads_recipes(self):
        category = Categoria.objects.create(name='Categoria')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe =Receita.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        )
        assert 1 == 1