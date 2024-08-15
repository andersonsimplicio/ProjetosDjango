from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
   

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente, related_name='Categoria')
    imagem = models.ImageField(upload_to='Categorias/')

    def __str__(self):
        return self.nome