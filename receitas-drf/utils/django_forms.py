import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def get_email(_email:str)->bool:
    user = User.objects.filter(email=_email)
    print(_email)
    print(user)
    return False


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val) 

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def strong_password(password):
       regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
       if not regex.match(password):
           raise ValidationError((
                'A senha deve ter pelo menos uma letra maiuscula', 
                'uma letra minuscula e um número. O comprimento deve ser',
                'de pelo menos 8 caracteres'
               ),
                code='invalid'
            )