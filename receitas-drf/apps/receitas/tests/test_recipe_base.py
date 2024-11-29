from django.test import TestCase
from apps.receitas.models import Categoria, Receita,User


class RecipeTestBase(TestCase):
    
    def setUp(self) -> None:
        category = Categoria.objects.create(name='Categoria')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='usernameteste',
            password='123456',
            email='username@email.com',
        )
        recipe = Receita.objects.create(
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

        # Imprime o ID da receita criada
        print(f"ID da receita criada: {recipe.id}")
        return super().setUp()