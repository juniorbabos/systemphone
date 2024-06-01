from __future__ import unicode_literals
from django.db import models
from django.utils.safestring import mark_safe
from estoque.models import Product
from cliente.models import Cliente

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = u'Fornecedor'
        verbose_name_plural = u'FORNECEDOR'
        



class Compra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    nota_fiscal = models.CharField(max_length=10)
    data = models.DateField()
    valor_compra = models.DecimalField(max_digits=10,
    decimal_places=2, blank=True, default=0)
    

    def imprimir(self):
            return mark_safe("""<a href=\"/orcamento/%s/\" target="_blank"><img src=\"/static/images/b_print.png\"></a>""" % self.id)

    class Meta:
        verbose_name = u'Compra'
        verbose_name_plural = u'COMPRAS'
        ordering = ['-data']

#classe venda
class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nota_fiscal = models.CharField(max_length=10)
    data = models.DateField()
    valor_venda = models.DecimalField(max_digits=10,
    decimal_places=2, blank=True, default=0)
    

    def imprimir(self):
            return mark_safe("""<a href=\"/transacao/venda/%s/\" target="_blank"><img src=\"/static/images/b_print.png\"></a>""" % self.id)


    class Meta:
        verbose_name = u'Venda'
        verbose_name_plural = u'VENDAS'
        ordering = ['-data']
    
    def __str__(self):
        return self.nota_fiscal

class ProdutoVenda(models.Model):
    material = models.ForeignKey(Product, on_delete=models.CASCADE)
    preco = models.DecimalField(u'PREÇO',max_digits=15,decimal_places=2)
    quantidade = models.DecimalField(u'QUANTIDADE', max_digits=5,decimal_places=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,
    editable=False)
    compra = models.ForeignKey(Venda, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Produto'
        verbose_name_plural = u'PRODUTOS'

    #calculo subtotal do orcamento
    #def save1(self, *args, **kwargs):
    #	self.subtotal = self.preco * self.quantidade 
    #	self.compra.valor_compra += self.subtotal
    #	self.compra.save() 
    #	return super(Produto, self).save(*args, **kwargs)
    
    #calculo e envio para incluir no estoque da tabela
    def save(self, *args, **kwargs):     
        self.subtotal = self.material.estoque_atual - self.quantidade
        self.material.estoque_atual = 0
        self.material.estoque_atual += self.subtotal
        self.material.save()
        self.subtotal = self.preco * self.quantidade
        self.compra.valor_venda += self.subtotal
        self.compra.save()
        
        return super(ProdutoVenda, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.material.name_product + ",R$" + str(self.preco) +"," + str(self.quantidade) + ",R$" + str(self.subtotal)

#FIM FUNCAO DE VENDA

class Produto(models.Model):
    material = models.ForeignKey(Product, on_delete=models.CASCADE)
    preco = models.DecimalField(u'PREÇO',max_digits=15,decimal_places=2)
    quantidade = models.DecimalField(u'QUANTIDADE', max_digits=5,decimal_places=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,
    editable=False)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Produto'
        verbose_name_plural = u'PRODUTOS'

    #calculo subtotal do orcamento
    #def save1(self, *args, **kwargs):
    #	self.subtotal = self.preco * self.quantidade 
    #	self.compra.valor_compra += self.subtotal
    #	self.compra.save() 
    #	return super(Produto, self).save(*args, **kwargs)
    
    #calculo e envio para incluir no estoque da tabela
    def save(self, *args, **kwargs):     
        self.subtotal = self.material.estoque_atual + self.quantidade
        self.material.estoque_atual = 0
        self.material.estoque_atual += self.subtotal
        self.material.save()
        self.subtotal = self.preco * self.quantidade
        self.compra.valor_compra += self.subtotal
        self.compra.save()
        
        return super(Produto, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.material.name_product + ",R$" + str(self.preco) +"," + str(self.quantidade) + ",R$" + str(self.subtotal)
