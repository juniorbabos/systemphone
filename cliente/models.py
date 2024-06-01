from django.db import models

# Create your models here.
#classe cliente

class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
    telefone = models.CharField(verbose_name="Telefone",max_length=100)
    cpf = models.CharField(max_length=100, null=True)
    endereco = models.CharField(verbose_name="Endereço", max_length=200)
    data_criada = models.DateField(verbose_name="Data de Criação",auto_now_add=True, null=False, blank=False)

    #CIDADE / BAIRRO 
   
   #responsavel para mostrar o nome correto no retorno
    def __str__(self):
        return self.nome