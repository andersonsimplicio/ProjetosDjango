from django import forms

from django.contrib.auth.models import User

def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val) 

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

class RegisterForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: Arthur')
        add_placeholder(self.fields['last_name'], 'Ex.: Simplico')
        add_attr(self.fields['username'], 'css', 'a-css-class')
        
        password = forms.CharField(
            required=True,
            widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}),
            error_messages={'required': 'Password must not be empty'},
            help_text=('A senha deve ter pelo menos uma letra maiúscula, ''uma letra minúscula e um número. O comprimento deve ser'
                'de pelo menos 8 caracteres' )
            )
        password2 = forms.CharField(
            required=True,
            widget=forms.PasswordInput(attrs={'placeholder': 'Repeat your password'})
        ) 
        
        
        
    class Meta:
        model=User
     
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
       
        # exclude = ['first_name']
        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'E-mail',
            'password': 'Password',
        }
        help_texts = {
            'email': 'O email válido: e.g. nome@email.com',
        }
        error_messages = {
            'username': {
                'required': 'Este campos não pode ser vazio.',
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Entre com nome de usuário',
                'class': 'input text-input'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha aqui'
            })
        }