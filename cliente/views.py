from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from estoque import views as v
#para reconhecer os name na urls precisa importar o reverse_lazy
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class SearchMixin:
    # buscar do cliente
    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        buscar = self.request.GET.get('buscar')
        if buscar:
            return queryset.filter(
                Q(nome__icontains=buscar) |
                Q(telefone__icontains=buscar) |
                Q(cpf__icontains=buscar)
            )
        return queryset
    # fim buscar do cliente

#class  base de views utilizando a class Clients
class ClientListView(LRM, SearchMixin, ListView):
    model = Cliente
    template_name = 'cliente_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#class para criarmos novos clientes
class ClientCreateView(SuccessMessageMixin, CreateView):
    model = Cliente
    fields = ["nome","telefone","endereco","cpf"]

    def get_success_url(self):
        return reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        contexto = super(ClientCreateView, self).get_context_data(**kwargs)
        contexto['action'] = reverse_lazy('clientes')
        return contexto

    success_message = 'Cliente cadastrado com sucesso!'
#success_url = reverse_lazy("clientes")

#class para fazer alterações no cliente
class ClientUpdateView(SuccessMessageMixin,UpdateView,ListView):
    model = Cliente
    fields = ["nome","telefone","cpf","endereco"]

    def get_success_url(self):
        return reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        contexto = super(ClientUpdateView, self).get_context_data(**kwargs)
        contexto['action'] = reverse_lazy('clientes')
        return contexto

    success_message = 'Cliente alterado com sucesso'

#c class para realizar o delete do cliente
class ClientDeleteView(SuccessMessageMixin,DeleteView):
    model = Cliente

    def get_success_url(self):
        return reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        contexto = super(ClientDeleteView, self).get_context_data(**kwargs)
        contexto['action'] = reverse_lazy('clientes')
        return contexto
    success_message = 'Cliente foi deletado com sucesso'

