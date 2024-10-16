from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
def caminho(instance, filename):
    # 'instance' é a instância do modelo Documento
    # 'filename' é o nome do arquivo original
    return f'{instance.usuario.username}/{instance.nome}/{filename}'

class Fotografia(models.Model):
    opcoes_categoria =[
        ("NEBULOSA","nebulosa"),
        ("ESTRELA","estrela"),
        ("GALAXIA","galaxia"),
        ("PLANETA","planeta")
    ]
    
    nome = models.CharField(max_length=100,blank=True,null=False)
    legenda = models.CharField(max_length=150,blank=True,null=False)
    categoria = models.CharField(max_length=150,choices=opcoes_categoria,default="galaxia")
    descricao = models.TextField(blank=True,null=False)
    foto = models.ImageField(upload_to=caminho,blank=True,null=False)
    publicada = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now,blank=False)
    usuario = models.ForeignKey(to=User,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=False,
                                related_name="user")


    def __str__(self) -> str:
        return f"Fotografia [nome={self.nome}]"
