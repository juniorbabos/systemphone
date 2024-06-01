# -*- Mode: Python; coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DeleteView
from .models import Fornecedor, Compra, Produto, Product, Venda
from django.contrib.auth.mixins import LoginRequiredMixin as LRM



class SearchMixin:
    # buscar do orcamento
    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        buscar = self.request.GET.get('buscar')
        if buscar:
            return queryset.filter(
                Q(nome__icontains=buscar) |
                Q(nota_fiscal__icontains=buscar) 
            )
        return queryset
    # fim buscar do orcamento


@login_required(redirect_field_name='redirect_to')
def orcamento(request, id=None, *args, **kwargs):
	contexto = {}
	contexto['orcamento'] = Compra.objects.get(id=id)

	return render(request, "orcamento.html", contexto)


#class  base de views utilizando a class Clients
class TransacaoListView(LRM, ListView, SearchMixin):
    model = Compra
    template_name = 'compras_list.html'

    #queryset = Compra.objects.filter(data__contains=)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def transacao_detail(request, pk):
    template_name = 'transacao/orcamento_detail.html'
    instance = Compra.objects.get(pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


#c class para realizar o delete 
class TransacaoDeleteView(DeleteView):
    model = Compra
    success_url = reverse_lazy("listar_orcamento")

class FornecedorCreateView(CreateView):
     model = Fornecedor
     fields = ['nome']
     success_url = reverse_lazy('home')

class FornecedorListView(LRM, ListView, SearchMixin):
    model = Fornecedor
    template_name = 'fornecedor_list.html'
    # buscar do orcamento
    # fim buscar do orcamento
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class VendaCreateView(CreateView):
    model = Venda
    fields = ['nota_fiscal','data','cliente']

   # def get_context_data(self, **kwargs):
        
    #    queryset = Product.objects.filter(material__contains=pk)

     #   return super().get_context_data(**kwargs)