from django import forms
from apps.receitas.models import Receita
from utils.django_forms import add_attr

from collections import defaultdict
from django.core.exceptions import ValidationError
from utils.strings import is_positive_number
from apps.authors.validators import AuthorRecipeValidator

class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._my_errors = defaultdict(list)
        add_attr(self.fields.get('preparation_steps'), 'class', 'span-2')
    
        
    class Meta:
        model = Receita
        fields = 'title', 'description', 'preparation_time', \
            'preparation_time_unit', 'servings', 'servings_unit', \
            'preparation_steps', 'cover'
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'servings_unit': forms.Select(
                choices=(
                    ('Porções', 'Porções'),
                    ('Pedaços', 'Pedaços'),
                    ('Pessoas', 'Pessoas'),
                ),
            ),
            'preparation_time_unit': forms.Select(
                choices=(
                    ('Minutos', 'Minutos'),
                    ('Horas', 'Horas'),
                ),
            ),
        }
    
    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        AuthorRecipeValidator(self.cleaned_data, ErrorClass=ValidationError)
        return super_clean
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._my_errors['title'].append('Must have at least 5 chars.')
        return title
    
    def clean_preparation_time(self):
        field_name = 'preparation_time'
        field_value = self.cleaned_data.get(field_name)
        if not is_positive_number(field_value):
            self._my_errors[field_name].append('Must be a positive number')
        return field_value
    
    def clean_servings(self):
        field_name = 'servings'
        field_value = self.cleaned_data.get(field_name)
        if not is_positive_number(field_value):
            self._my_errors[field_name].append('Must be a positive number')
        return field_value