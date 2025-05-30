from time import sleep
from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

class AuthorsRegisterTest(AuthorsBaseTest):
        
    def fill_form_dummy_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')
        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)
                
    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )
    
    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()
        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('dummy@email.com')
        
        callback(form)
        return form
        
    def test_empty_first_name_error_message(self):
        
        def callback(form):
            first_name_field = self.get_by_placeholder(form, 'Ex.: Arthur')
            first_name_field.clear()
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Escreva seu primeiro nome', form.text)
        self.form_field_test_with_callback(callback)
        
        
    def test_empty_last_name_error_message(self):
        
        def callback(form):
            last_name_field = self.get_by_placeholder(form, 'Ex.: Simplico')
            last_name_field.clear()
            last_name_field.send_keys(' '*20)
            last_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Escreva seu último nome', form.text)
        self.form_field_test_with_callback(callback)
    
    def test_empty_username_error_message(self):
        
        def callback(form):
            username_field = self.get_by_placeholder(form, 'Your username')
            username_field.clear()
            username_field.send_keys(' '*10)
            username_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Password não deve estar vazio!', form.text)
        self.form_field_test_with_callback(callback)
        
        
    def test_invalid_email_error_message(self):
       
        def callback(form):
            email_field = self.get_by_placeholder(form, 'Your e-mail')
            email_field.clear() 
            email_field.send_keys('email@invalid')
            email_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Não sabe escrever não?', form.text)
            
        self.form_field_test_with_callback(callback)

        
    def test_passwords_do_not_match(self):
        def callback(form):
            password1 = self.get_by_placeholder(form, 'Senha')
            password2 = self.get_by_placeholder(form, 'Confirme a senha.')
            password1.send_keys('P@ssw0rd')
            password2.send_keys('P@ssw0rd_Different')
            password2.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Password and password2 must be equal', form.text)
        self.form_field_test_with_callback(callback)
        
        
    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()
        self.get_by_placeholder(form, 'Ex.: Arthur').send_keys('First Name')
        self.get_by_placeholder(form, 'Ex.: Simplico').send_keys('Last Name')
        self.get_by_placeholder(form, 'Your username').send_keys('my_username')
        self.get_by_placeholder(
            form, 'Your e-mail').send_keys('email@valid.com')
        self.get_by_placeholder(form, 'Senha').send_keys('P@ssw0rd1')
        self.get_by_placeholder(form, 'Confirme a senha.').send_keys('P@ssw0rd1')
        form.submit()
        self.assertIn(
            'Seu usuário foi criado, faça o login.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )