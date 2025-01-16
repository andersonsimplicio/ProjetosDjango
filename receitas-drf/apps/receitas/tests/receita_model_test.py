from django.test import TestCase
from django.urls import reverse
#Nunca esquecer de passa caminho absoluto apps...
from apps.receitas.models import Categoria, Receita, User
'''
Comando para realizar test utilizando o covarage

coverage run manage.py test apps/receitas/tests/

coverage cria uma lista de teste feitos no projeto.
'''
class ReceitaModelTest(TestCase):
    
    def test_recipe_home_template_loads_recipes(self):
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

        # Tenta acessar a URL da receita criada
        url = reverse('apps.receitas:receita', kwargs={"id": recipe.id})
        print(f"URL gerada: {url}")

        # Faz a requisição
        response = self.client.get(url)

        # Verifica o conteúdo da resposta
        content = response.content.decode('utf-8')
        #print(f"Conteúdo retornado: {content}")

        # Verifica o contexto da resposta
        response_context_recipes = response.context.get('receita')
        print(f"Receitas no contexto da resposta: {response_context_recipes}")
        
       
        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
       
        self.assertEqual(len([response_context_recipes]), 1)
        '''
         
         with open('apps/receitas/test/response_test_output.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        '''