from django.contrib import admin
from .models import Product
from estoque.models import Product, Categoria
from cliente.models import Cliente
from servico.models import Servico, OrdemServico
from estoque.models import SaidaEstoque, EntradaEstoque
#from transacao.models import EntradaEstoque, SaidaEstoque
from transacao.models import Fornecedor,Compra, Produto, Product, Venda, ProdutoVenda

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('codigo_barra','name_product','categoria','estoque_atual','estoque_min','valor_venda','valor_custo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','cpf','endereco','data_criada')

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','cliente','situacao','data')
#'valor',"valor_custo","valor_lucro"
#@admin.register(EntradaEstoque)
#class EntradaEstoqueAdmin(admin.ModelAdmin):
 #   list_display = ('produto','quantidade','criado_em')

#@admin.register(SaidaEstoque)
#class SaidaEstoqueAdmin(admin.ModelAdmin):
 #   list_display = ('produto','quantidade','os','cliente','criado_em')

admin.site.register(Categoria)
admin.site.register(Servico)


class ProdutoAdmin(admin.TabularInline):

	model = Produto
	extra = 1

class ProdutovendaAdmin(admin.TabularInline):

	model = ProdutoVenda
	extra = 1

class FornecedorAdmin(admin.ModelAdmin):
	pass

class MaterialAdmin(admin.ModelAdmin):
	pass

class CompraAdmin(admin.ModelAdmin):

	date_hierarchy = 'data'
	list_filter = ['data', 'fornecedor']

	inlines = [ProdutoAdmin]
	list_display = ['data', 'nota_fiscal', 'fornecedor', 'valor_compra', 'imprimir']
	
class VendaAdmin(admin.ModelAdmin):

	date_hierarchy = 'data'
	list_filter = ['data', 'cliente']

	inlines = [ProdutovendaAdmin]
	list_display = ['data', 'nota_fiscal', 'cliente', 'valor_venda', 'imprimir']



admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Venda, VendaAdmin)



@admin.register(SaidaEstoque)
class SaidaEstoqueAdmin(admin.ModelAdmin):
    list_display = ('descricao','saida','quantidade','data','saldo')


@admin.register(EntradaEstoque)
class EntradaEstoqueAdmin(admin.ModelAdmin):
    list_display = ('descricao','entrada','quantidade','data','saldo')



