from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"e. g. Anderson"
            }
        )
        )
    
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"digite sua senha"
            }
        )
        )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"e. g. Anderson"
            }
        )
        )
    
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"e. g. anderson@email.com"
            }
        )
        )
    
    senha1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "style":"color:#D9D9D9; margin-bottom: 5px;",
                "placeholder":"digite sua senha"
            }
        )
        )
    
    senha2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "style":"color:#D9D9D9; margin-bottom: 5px;",
                "placeholder":"digite sua senha"
            }
        )
        )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        if nome:
            nome = nome.strip()
            nome.replace(" ","_")
            print(nome)
            if " " in nome:
                raise forms.ValidationError("Não é possivél inserir espaços dentro campo nome de usuário")
            else:
                return nome
    
    def clean_senha2(self):
        senha1 = self.cleaned_data.get('senha1')
        senha2 = self.cleaned_data.get('senha2')

        if senha1 and senha2:
                if senha1 !=senha2:
                     raise forms.ValidationError("Senhas não são iguais")
                else:
                    return senha2