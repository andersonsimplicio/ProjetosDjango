from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from utils.django_forms import add_placeholder, get_email,strong_password

class RegisterForms(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: Arthur')
        add_placeholder(self.fields['last_name'], 'Ex.: Simplico')
        add_placeholder(self.fields['password'],'Senha')
        add_placeholder(self.fields['password2'], 'Confirme a senha.')
        
    password = forms.CharField(
        #required=True,
        widget=forms.PasswordInput(),
        error_messages={'required': 'Password não deve estar vazio!'},
        help_text=('A senha deve ter pelo menos uma letra maiuscula', 
                    'uma letra minuscula e um número. O comprimento deve ser',
                    'de pelo menos 8 caracteres' ),
            validators=[strong_password],
            label='Senha'
        )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Confirme a senha.',
        error_messages={'required': 'Confirme a senha.'},
    )
    first_name = forms.CharField(
    error_messages={'required': 'Escreva seu primeiro nome'},
    label='Nome'
    )
    last_name = forms.CharField(
        error_messages={'required':'Escreva seu último nome'},
        label='Sobrenome'
    )
    email = forms.EmailField(
        error_messages={'required': 'E-mail é necessário','invalid':'Não sabe escrever não?'},
        label='E-mail',
        help_text='O email válido: e.g. nome@email.com',
    )
    
    username = forms.CharField(
        label='Nome de usuário',
        help_text= (
            "Nome de usuário deve conter letras, números ou um destes caracteres:",
            "@.+-_. O comprimento deve estar entre 4 e 150 caracteres."),
        error_messages={
            'required': 'Este campo não pode ser vazio.',
            'min_length': 'O nome de usuário deve ter pelo menos 4 caracteres',
            'max_length': 'O nome de usuário deve ter menos de 150 caracteres',
        },
        min_length=4, max_length=150,
    )
    class Meta:
        model=User
     
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password2'
        ]
       
        
        help_texts = {
           # 'email':'O email válido: e.g. nome@email.com',
           # 'password':('A senha deve ter pelo menos uma letra maiuscula', 
           # 'uma letra minuscula e um número. O comprimento deve ser',
           # 'de pelo menos 8 caracteres')
        }
    
    def clean_email(self):
        _email = self.cleaned_data.get('email')
       
        email_user = get_email(_email)
        if email_user:
            raise ValidationError("Este e-mail já está registrado. Por favor, use outro e-mail.")
        return _email
    
    def clean(self):
        cleaned_data = super().clean()        
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
    
        
   
    
   
    