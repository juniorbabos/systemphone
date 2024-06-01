from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Product, Categoria, EntradaEstoque, SaidaEstoque
from cliente.models import Cliente
from transacao.models import Compra, Fornecedor, ProdutoVenda,ProdutoVenda, Venda
from django.http import HttpResponse
from django.db.models import Q, Avg, Sum, Count
from datetime import datetime
from datetime import timedelta
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin as LRM


class SearchMixin:
    # buscar 
    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        buscar = self.request.GET.get('buscar')
        if buscar:
            return queryset.filter(
                Q(name_product__icontains=buscar) |
                Q(codigo_barra__icontains=buscar) |
                Q(descricao__icontains=buscar)
            )
        return queryset
    # fim buscar 


#class para listar os produtos em formado de tabelas ordenadas
class ProdutoList(LRM, SearchMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 10

    def get_queryset(self):
            queryset = super(ProdutoList, self).get_queryset()
            search = self.request.GET.get('search')
            if search:
                queryset = queryset.filter(
                    Q(name_product__icontains=search) |
                    Q(codigo_barra__icontains=search) |
                    Q(categoria__icontains=search) |
                    Q(descricao__icontains=search)
                )
            return queryset

    
 

#class para criarmos novos produtos 
class ProdutoCreateView(SuccessMessageMixin,CreateView):
    model = Product
    fields = ["name_product","categoria","descricao","codigo_barra","estoque_min","estoque_atual","valor_custo","valor_venda"]
    
    def get_success_url(self):
        return reverse_lazy('home_estoque')

    def get_context_data(self, **kwargs):
        contexto = super(ProdutoCreateView, self).get_context_data(**kwargs)
        contexto['action'] = reverse_lazy('home_estoque')
        return contexto
    success_message = 'Produto foi cadastrado com sucesso!'

#class para fazer alterações no produto
class ProductUpdateView(SuccessMessageMixin,UpdateView,ListView):
    model = Product
    fields = ["name_product","categoria","descricao","codigo_barra","estoque_min","estoque_atual","valor_custo","valor_venda"]

    def get_success_url(self):
        return reverse_lazy('home_estoque')

    def get_context_data(self, **kwargs):
        contexto = super(ProductUpdateView, self).get_context_data(**kwargs)
        contexto['action'] = reverse_lazy('home_estoque')
        return contexto
    success_message = 'Produto foi alterado com sucesso!'




#c class para realizar o delete do produto
class ProductDeleteView(SuccessMessageMixin,DeleteView):
    model = Product

    def get_success_url(self):
        return reverse_lazy('home_estoque')

    def get_context_data(self, **kwargs):
        contexto = super(ProductDeleteView, self).get_context_data(**kwargs)
        contexto['action'] = reverse_lazy('home_estoque')
        return contexto
    success_message = 'Produto foi deletado com sucesso!'

#class para cadastrar Categoria 
class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['categoria']
    success_url = reverse_lazy("cadastrar_produto")

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    paginate_by = 100

#class home para listar 
def home(request):
    context = {
        "home": home,
        "calculo": SaidaEstoque.objects.aggregate(Sum('subtotal')),
    }
    

    return render(request, "index.html", context)


#class home para listar 
def graficos(request):
    context = {
        "graficos": graficos,
        "calculo": SaidaEstoque.objects.aggregate(Sum('subtotal')),
        "produtos": Product.objects.aggregate(Sum('estoque_atual')),
        "qnt_produtos": Product.objects.all().count(),
        "clientes": Cliente.objects.all().count(),
        "comprasrs": Compra.objects.aggregate(Sum('valor_compra')),
        "vendasrs": Venda.objects.aggregate(Sum('valor_venda')),
        "qnt_saida": SaidaEstoque.objects.aggregate(Sum('quantidade')),
        "qnt_entrada": EntradaEstoque.objects.aggregate(Sum('quantidade')),
        "fornecedor": Fornecedor.objects.all().count(),
        "vendas_mes": SaidaEstoque.objects.filter(data__gte=datetime.today()-timedelta(days=30)).values('status').aggregate(Sum('subtotal')),
    }
    

    return render(request, "graficos.html", context)

#class UltimasVendas(ListView):
    #model = SaidaEstoque
    #queryset = SaidaEstoque.objects.filter(data__gte=datetime.today()-timedelta(days=30)).values('status').annotate(Sum('subtotal')),
    #template_name ='estoque/ultimas_vendas.html'
    
def vendas(request):
    context = {
        "vendas": vendas,
        "vendas_mes": SaidaEstoque.objects.filter(data__gte=datetime.today()-timedelta(days=30)).annotate(Sum('subtotal')),
    }
    return render(request, "estoque/ultimas_vendas.html", context)

class EntradaCreateView(CreateView):
    model = EntradaEstoque
    fields = ['descricao','entrada', 'quantidade']
    success_url = reverse_lazy("home_estoque")

class SaidaCreateView(CreateView):
    model = SaidaEstoque
    fields = ['status','descricao','saida', 'quantidade','preco']
    success_url = reverse_lazy("home_estoque")
 
class SaidaListView(ListView):
    model = SaidaEstoque
    paginate_by = 100
    template_name = 'saida_list.html'

    def calcularsaida(request):
        result = SaidaEstoque.objects.aggregate(Sum('subtotal'))
        return result
        

class EntradaListView(ListView):
    model = EntradaEstoque
    paginate_by = 100
    template_name = 'entrada_list.html'

def calcularsaida(request):
    
    result = SaidaEstoque.objects.aggregate(Sum('subtotal'))

    return HttpResponse(f'Resultado:{result}')
