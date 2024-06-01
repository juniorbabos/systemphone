
from django.contrib import admin
from django.urls import path,include
from estoque import views as v
from cliente import views as c
from servico import views as s
from transacao import views as t
from cliente.views import ClientListView, ClientCreateView, ClientDeleteView, ClientUpdateView
from estoque.views import ProdutoList, ProdutoCreateView, CategoriaCreateView, EntradaCreateView, SaidaCreateView, SaidaListView, EntradaListView, calcularsaida, graficos,UpdateView,vendas
from transacao.views import orcamento,TransacaoListView,transacao_detail, TransacaoDeleteView,FornecedorCreateView,FornecedorListView, VendaCreateView


urlpatterns = [
    #urls admin
    path('admin/', admin.site.urls),
    path('/accounts/login/', admin.site.urls),

    #URLS DO ESTOQUE
    path('estoque/', v.ProdutoList.as_view(), name="home_estoque"),
    path('estoque/grafico',v.calcularsaida, name='estoque_grafico'),
    path('ultimasvendas', v.vendas, name='ultimasvendas'),
    path ('estoque/cadastro', v.ProdutoCreateView.as_view(), name="cadastrar_produto"),
    path('servico/form_ordenservico', s.form_ordenservico, name="form_ordenservico"),
    path('atualiza_produto/<int:pk>', v.ProductUpdateView.as_view(), name="atualiza_produto"),
    path('delete/<int:pk>',v.ProductDeleteView.as_view(), name="delete_produto"),
    path ('estoque/cadastro_categoria', v.CategoriaCreateView.as_view(), name="cadastro_categoria"),
    path ('estoque/listar_categoria', v.CategoriaListView.as_view(), name="listar_categoria"),
    path('', v.home, name="home"),
    path('graficos', v.graficos, name="graficos"),
    path('estoque/entrada', EntradaCreateView.as_view(), name="criar_entrada_estoque"),
    path('estoque/saida', SaidaCreateView.as_view(), name="criar_saida_estoque"),
    path('estoque/listar_saida', SaidaListView.as_view(), name="listar_saida"),
    path('estoque/listar_entrada', EntradaListView.as_view(), name="listar_entrada"),

    #URLS dos clientes
    path('cliente/', c.ClientListView.as_view(), name="clientes"),
    path ('cadastrar_cliente', c.ClientCreateView.as_view(), name="cadastrar_cliente"),
    path('atualiza_cliente/<int:pk>', c.ClientUpdateView.as_view(), name="atualiza_cliente"),
    path('delete_cliente/<int:pk>', c.ClientDeleteView.as_view(), name="delete_cliente"),

    #URLS dos serviços
      path('servico/', s.ordem_servico_list, name='home_servicos'),  # noqa E501
      path('servico/cadastrar_ordemservico', s.OrdenServicoCreateView.as_view(), name='ordem_servico_create'),  # criacao do serviço
      path('visualizar_os/<int:pk>', s.ordem_servico_detail, name="visualizar_os"),
      path('servico/criar', s.ServicoCreateView.as_view(), name="cadastrar_servico"),
      path('servico/finalizar_os/<int:pk>', s.OrdenServicoUpdateView.as_view(), name="finalizar_os"),

    #URLS ORÇAMENTO
    path('orcamento/<int:id>/', t.orcamento, name='orcamento'),
    path('transacao/listar_orcamentos/', t.TransacaoListView.as_view(), name='listar_orcamento'),
    path('trasancao/<int:id>/', t.transacao_detail, name='visualizar_orcamento'),
    path('delete_orcamento/<int:pk>', t.TransacaoDeleteView.as_view(), name="delete_orcamento"),
    path('transacao/criar_venda', t.VendaCreateView.as_view(), name="cadastrar_venda"),

     #URL FORNECEDOR
    path('cadastro_fornecedor', t.FornecedorCreateView.as_view(), name='cadastrar_fornecedor'),
    path('visualizar_fornecedor', t.FornecedorListView.as_view(), name='listar_fornecedor'),
]
