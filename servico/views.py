from django.shortcuts import render
from django.urls import reverse_lazy
from datetime import datetime
from .forms import OrdemServicoForm, forms
from datetime import timedelta
from django.views import generic
from servico.forms import OrdemServicoForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

#from .forms import OrdemServicoForm
from .models import OrdemServico, Servico


def ordem_servico_list(request):

    
    template_name = 'servico/ordem_servico_list.html'
    object_list = OrdemServico.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(situacao=search)

    context = {'object_list': object_list}
    return render(request, template_name, context)


#class para fazer alterações no cliente
class OrdenServicoUpdateView(SuccessMessageMixin,UpdateView):
    model = OrdemServico
    fields = ["situacao","solucao","valor_custo","valor","data_termino"]

    def get_success_url(self):
        return reverse_lazy('home_servicos')

    def get_context_data(self, **kwargs):
        contexto = super(OrdenServicoUpdateView, self).get_context_data(**kwargs)
        contexto['action'] = reverse_lazy('home_servicos')
        return contexto

    success_message = 'Ordem de serviço finalizada!'



class OrdenServicoCreateView(SuccessMessageMixin,CreateView):
    model = OrdemServico
   # template_name = 'formulario_os.html'
    fields = ["servico","cliente","situacao","observacao"]
    
    def get_success_url(self):
        return reverse_lazy('home_servicos')

    def get_context_data(self, **kwargs):
        contexto = super(OrdenServicoCreateView, self).get_context_data(**kwargs)
        contexto['action'] = reverse_lazy('home_servicos')
        return contexto
    success_message = 'Ordem de serviço criada com sucesso!'


'''class FormularioOS(CreateView, forms.ModelForm):
    servico = forms.Select()
    situacao = forms.Select()

    class Meta:
        model = OrdemServico
        fields = [
            'servico',
            'situacao'
        ]'''


def form_ordenservico(request):
    
    if request.method == "GET":
        form = OrdemServicoForm()
        context = {
            'form': form
        }
        return render(request, "servico/formulario_os.html", context=context)
    else:
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            ordenservico = form.save()
            form = OrdemServicoForm()
        
        context = {
            'form': form
        }
        return render(request, "servico/formulario_os.html", context=context)


def ordem_servico_detail(request, pk):

    template_name = 'servico/ordem_servico_detail.html'
    instance = OrdemServico.objects.get(pk=pk)  
   
    context = {'object': instance,   
    }


    return render(request, template_name, context)


class ServicoCreateView(CreateView):
    model = Servico
    fields = ["servico"]
    success_url = reverse_lazy("home")


#


#class RelatorioServicoListView(generic.ListView):

 #   queryset = OrdemServico.objects.filter(creation_date__gte=datetime.today()-timedelta(days=30))
  #  context_object_name = 'osss'
   # template_name = 'relatorio_os.html'
