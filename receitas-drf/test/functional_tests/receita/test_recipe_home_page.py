from time import sleep
from selenium.webdriver.common.by import By
from .base import RecipeBaseFunctionalTest
import pytest
from unittest.mock import patch
from selenium.webdriver.common.keys import Keys


'''
Comando para rodar apenas os testes com mark funcional
pytest -m 'functional_test' -rP
no arquivo pytest.ini deve ser acrescentado:
markers =
... outras coisas
functional_test: Run tests that are selenium based

para rodar o contrário
pytest -m 'not functional_test' -rP
'''

@pytest.mark.functional_test 
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    
    
    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Receitas\nNão existe receitas 🥲\n', body.text)
   
    @patch('apps.receitas.views.PER_PAGE', new=2)
    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch()
        title_needed = 'This is what I need'
        recipes[0].title = title_needed
        recipes[0].save()
        # Usuário abre a página
        self.browser.get(self.live_server_url)
        # Vê um campo de busca com o texto "Search for a recipe"
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Busca por receita"]'
        )
        # Clica neste input e digita o termo de busca
        # para encontrar a receita o título desejado
        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)
        # O usuário vê o que estava procurando na página
        self.assertIn(
            title_needed,
            self.browser.find_element(By.CLASS_NAME, 'main-content-list').text,
        )
        sleep(6)
        
    @patch('apps.receitas.views.PER_PAGE', new=2)
    def test_recipe_home_page_pagination(self):
        self.make_recipe_in_batch()
        # Usuário abre a página
        self.browser.get(self.live_server_url)
        # Vê que tem uma paginação e clica na página 2
        page2 = self.browser.find_element(
            By.XPATH,
            '//a[@aria-label="Go to page 2"]'
        )
        page2.click()
        # Vê que tem mais 2 receitas na página 2
        self.assertEqual(
            len(self.browser.find_elements(By.CLASS_NAME, 'recipe')),
            2
        )
        sleep(10)