#declarando models
from django.db import models
from django.urls import reverse_lazy
from datetime import date

class Product(models.Model):

    name_product = models.CharField(verbose_name="Produto", max_length=150, null=False, blank=False)
    descricao = models.CharField(max_length=250, null=True)
    codigo_barra = models.CharField(max_length=50, null=True)
    estoque_min = models.IntegerField(null=True)
    estoque_atual = models.PositiveIntegerField(null=True)
    valor_custo = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    valor_venda = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name_product',)
        verbose_name = u'Produto'
        verbose_name_plural = u'PRODUTOS'

    def __str__(self):
        return self.name_product
    def get_absolute_url(self):
        return reverse_lazy('product_name:produto_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'product_name': self.name_product,
            'estoque_atual': self.estoque_atual,
        }


class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return self.categoria

class SaidaEstoque(models.Model):
    descricao = models.CharField(max_length=200, unique=True)
    saida = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade =  models.IntegerField(null=True)
    preco = models.DecimalField(u'PREÇO',max_digits=15,decimal_places=2, default=0)
    saldo = models.IntegerField(null=True, default=0)
    data = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField(verbose_name="Venda", null=False, default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,
    editable=False, default=0)
    
    

    def save(self, *args, **kwargs):
        #pega o campo saldo n
        self.saldo = self.saida.estoque_atual - self.quantidade
        self.saida.estoque_atual = 0
        self.saida.estoque_atual += self.saldo
        self.subtotal = self.quantidade * self.preco
        self.saida.save()
        return super(SaidaEstoque, self).save(*args, **kwargs)

class EntradaEstoque(models.Model):
    descricao = models.CharField(max_length=200, unique=True)
    entrada = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade =  models.IntegerField(null=True)
    saldo = models.IntegerField(null=True, default=0)
    data = models.DateField(auto_now_add=True, null=True)
    

    def save(self, *args, **kwargs):
        #pega o campo saldo n
        self.saldo = self.entrada.estoque_atual + self.quantidade
        self.entrada.estoque_atual = 0
        self.entrada.estoque_atual += self.saldo
        self.entrada.save()
        return super(EntradaEstoque, self).save(*args, **kwargs)