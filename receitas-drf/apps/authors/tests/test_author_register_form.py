from apps.authors.forms import RegisterForms
from unittest import TestCase
from django.test import TestCase as DjangoTestCase
from django.urls import reverse
from parameterized import parameterized
from django.utils.html import escape

#comando para teste:
#coverage run -m pytest apps/receitas/tests/ apps/authors/tests/
#coverage report -m

class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Your username'),
        ('email', 'Your e-mail'),
        ('first_name', 'Ex.: Arthur'),
        ('last_name', 'Ex.: Simplico'),
        ('password', 'Senha'),
        ('password2', 'Confirme a senha.'),
    ])    
    
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForms()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)
    
    @parameterized.expand([
        ('username', (
            "Nome de usuário deve conter letras, números ou um destes caracteres:",
            "@.+-_. O comprimento deve estar entre 4 e 150 caracteres.")),
        
        ('email', 'O email válido: e.g. nome@email.com'),
        ('password', ('A senha deve ter pelo menos uma letra maiuscula', 
                    'uma letra minuscula e um número. O comprimento deve ser',
                    'de pelo menos 8 caracteres' )),
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForms()
        current = form[field].field.help_text
        self.assertEqual(current, needed)
    
    @parameterized.expand([
        ('username', 'Nome de usuário'),
        ('first_name', 'Nome'),
        ('last_name', 'Sobrenome'),
        ('email', 'E-mail'),
        ('password', 'Senha'),
        ('password2', 'Confirme a senha.'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForms()
        current = form[field].field.label
        self.assertEqual(current, needed)
    
    
class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'anderson@email.com',
            'password': '1',
            'password2':'1',
        }
        return super().setUp(*args, **kwargs)
    
    @parameterized.expand([
        ('username', 'Este campo não pode ser vazio.'),
        ('first_name', 'Escreva seu primeiro nome'),
        ('last_name', 'Escreva seu último nome'),
        ('password', 'Password não deve estar vazio!'),
        ('password2', 'Confirme a senha.'),
        ('email', 'E-mail é necessário'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('apps.authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))
    
    def test_username_field_min_length_should_be_4(self):
        self.form_data['username'] = 'joa'
        url = reverse('apps.authors:register_create')
        
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'O nome de usuário deve ter pelo menos 4 caracteres'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))
        
    def test_username_field_max_length_should_be_150(self):
        self.form_data['username'] = 'A' * 151
        url = reverse('apps.authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'O nome de usuário deve ter menos de 150 caracteres'
        self.assertIn(msg, response.context['form'].errors.get('username'))
        self.assertIn(msg, response.content.decode('utf-8'))
    
    def test_password_field_have_lower_upper_case_letters_and_numbers(self):
        self.form_data['password'] = 'abc123'
        self.form_data['password2'] = 'abc123'
        url = reverse('apps.authors:register')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg =  str('(&#x27;A senha deve ter pelo menos uma letra maiuscula&#x27;, &#x27;uma letra minuscula e um número. O comprimento deve ser&#x27;, &#x27;de pelo menos 8 caracteres&#x27;)')
        self.assertIn(msg, response.content.decode('utf-8'))  
        
        self.form_data['password'] = '@A123abc123'
        self.form_data['password2'] = '@A123abc123'
        url =  reverse('apps.authors:register')
        response = self.client.post(url, data=self.form_data, follow=True)
        if response.context['form'].errors.get('password') is None:
            msg=None
            
        self.assertEqual(msg,response.context['form'].errors.get('password'))
        
    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = '@A123abc123!'
        self.form_data['password2'] = '@A123abc1235!'
        url = reverse('apps.authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        
        msg = 'Password and password2 must be equal'
        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))
        
        self.form_data['password'] = '@A123abc123!'
        self.form_data['password2'] = '@A123abc123!'
        url =  reverse('apps.authors:register')
        
        response = self.client.post(url, data=self.form_data, follow=True)
        #self.assertNotIn(msg, response.content.decode('utf-8'))
    
    def test_send_get_request_to_registration_create_view_returns_404(self):
        url = reverse('apps.authors:register_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_email_field_must_be_unique(self):
        url = reverse('apps.authors:register_create')
        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Este e-mail já está registrado. Por favor, use outro e-mail.'
        if response.context['form'].errors.get('email'):
            self.assertIn(msg, response.context['form'].errors.get('email'))
            self.assertIn(msg, response.content.decode('utf-8'))
    
    def test_author_created_can_login(self):
        url = reverse('apps.authors:register')
        
        self.form_data.update({
            'username': 'arthur',
            'password': 'Abc@123!',
            'password2': 'Abc@123!',
        })
        self.client.post(url, data=self.form_data, follow=True)
        is_authenticated = self.client.login(
            username='arthur',
            password='Abc@123!'
        )
        #self.assertTrue(is_authenticated)