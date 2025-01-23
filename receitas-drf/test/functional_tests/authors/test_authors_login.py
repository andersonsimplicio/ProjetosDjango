from time import sleep
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By
from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = 'Abc@123!'
        user = User.objects.create_user(
            username='arthur', password=string_password
        )
        # Usuário abre a página de login
        self.browser.get(self.live_server_url + reverse('apps.authors:login'))
        # Usuário vê o formulário de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Your username')
        password_field = self.get_by_placeholder(form, 'Type your password')
        # Usuário digita seu usuário e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)
        # Usuário envia o formulário
        form.submit()
        # Usuário vê a mensagem de login com sucesso e seu nome
        self.assertIn(
            f'Você está logando como {user.username}.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
        
    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(
            self.live_server_url +
            reverse('apps.authors:login_create')
        )
        self.assertIn(
            'Not Found',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
    
    def test_form_login_invalid_credentials(self):
        # Usuário abre a página de login
        self.browser.get(
            self.live_server_url + reverse('apps.authors:login')
        )
        # Usuário vê o formulário de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        # E tenta enviar valores com dados que não correspondem
        username = self.get_by_placeholder(form, 'Your username')
        password = self.get_by_placeholder(form, 'Type your password')
        username.send_keys('invalid_user')
        password.send_keys('invalid_password')
        # Envia o formulário
        form.submit()
        # Vê uma mensagem de erro na tela
        self.assertIn(
            'Invalid credentials',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )