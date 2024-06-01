from django.db import models
from cliente.models import Cliente
from estoque.models import Product

# Create your models here.
class Servico(models.Model):
    servico = models.CharField(verbose_name="Serviço", max_length=150, null=False, blank=False)
    
    #responsavel para mostrar o nome correto no retorno
    def __str__(self):
        return self.servico
    
SITUACAO = (
    ('pe', 'Pendente'),
    ('ca', 'Cancelado'),
    ('an', 'Andamento'),
    ('ap', 'Aprovado'),
)



class OrdemServico(models.Model):
    situacao = models.CharField('Situação', max_length=2, choices=SITUACAO)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        verbose_name='cliente',
        related_name='clientes',
        null=True,
        blank=True
    )
    servico = models.ForeignKey(Servico, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    #produto = models.ForeignKey(Product, 
     #   on_delete=models.CASCADE,
      #  null=True,
       # blank=True
        #)
    #quantidade = models.PositiveIntegerField(verbose_name="quantidade", null=True, blank=True)
    #valor_produto = models.DecimalField('valor Produto', max_digits=10,
    #decimal_places=2, blank=True, default=0)

    #ocultar alguns campos aqui
    valor_custo = models.DecimalField('Valor Custo', max_digits=8, decimal_places=2, null=True, blank=True, default=0)
    valor_lucro = models.DecimalField('Valor Lucro', max_digits=8, decimal_places=2, null=True, blank=True, default=0)
    data = models.DateTimeField('Data do Serviço', auto_now_add=True, null=True, blank=True )
    observacao = models.TextField('Observação', null=True, blank=True)
    valor = models.DecimalField('Valor total', max_digits=10,
    decimal_places=2, blank=True, default=0)
    solucao = models.TextField('Solução', null=True, blank=True)
    data_termino = models.DateTimeField('Data do Término', null=True, blank=True )

    def save(self, *args, **kwargs):
        #pega o campo saldo n
        self.valor_lucro = self.valor - self.valor_custo
        return super(OrdemServico, self).save(*args, **kwargs)


    def __str__(self):
        return self.servico.servico



    

    


     
    




