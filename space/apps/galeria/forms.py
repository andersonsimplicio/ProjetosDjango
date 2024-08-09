from django import forms
from .models import Fotografia


class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada']
        labels = {
            'nome':"Nome da Figura",
            'descricao':'Descrição',
            'date':"Data de resgistro",
            "usuario":"usuário"
        }

        widgets = {
            'nome':forms.TextInput(attrs={"class":"form-control",}),
            "legenda":forms.TextInput(attrs={"class":"form-control",}),
            "categoria":forms.Select(attrs={"class":"form-control",}),
            "descricao":forms.Textarea(attrs={"class":"form-control",}),
            "foto":forms.FileInput(attrs={"class":"form-control",}),
            'usuario': forms.TextInput(attrs={
                "class": "form-control",
                "readonly": "readonly"  # Torna o campo somente leitura
            }),
            "date":forms.DateInput(
                format="%d/%m/%Y",
                attrs={
                    "type":"date",
                    "class":"form-control",     
                }
            )
                
        }
   
    