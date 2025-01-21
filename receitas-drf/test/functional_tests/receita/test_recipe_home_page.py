from selenium.webdriver.common.by import By
from .base import RecipeBaseFunctionalTest
import pytest
from unittest.mock import patch

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
    
    @patch('apps.receitas.views.PER_PAGE', new=2)
    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Receitas\n>\nNão existe receitas 🥲\n', body.text)
     
    @patch('apps.receitas.views.PER_PAGE', new=2) 
    def test_recipe_home_page_without_recipes_not_found_message_2(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')