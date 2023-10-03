from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    endereco = models.TextField()
    logradouro= models.TextField()
    telefone = models.CharField(max_length=13)
    email = models.EmailField()


    def __str__(sefl):
        return sefl.nome


class Compra(models.Model):
   
    produto = models.CharField(max_length=50)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    codigo = models.IntegerField()

    def __str__(sefl):
        return sefl.produto