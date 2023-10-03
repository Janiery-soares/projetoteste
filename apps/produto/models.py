from django.db import models

class Cliente(models.Model):
    lista_sexo = [
        ('M', 'masculino'),
        ('F', 'feminino'),
    ]
    nome_cliente = models.CharField(max_length=30)
    endereco = models.TextField()
    logradouro= models.TextField()
    idade = models.IntegerField() 
    sexo = models.CharField(max_length=1 , choices=lista_sexo)
    telefone = 
    email = models.EmailField()

    def __str__(self):
        return self.nome_cliente
    
class DadosPessoal(models.Model):
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=10)

    def __str__(sefl):
        return sefl.cpf


class Produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    valor_produto = models.DecimalField(decimal_places=2 , max_digits=7)
    descricao_produtp = models.TextField()
    codigo_produto = models.IntegerField()

    def __str__(self):
        return self.nome_produto
