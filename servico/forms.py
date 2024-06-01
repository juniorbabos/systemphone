from django import forms

from .models import OrdemServico

#fields = ["servico","cliente","situacao","data","observacao","valor_custo","valor"]

class OrdemServicoForm(forms.ModelForm):
    servico = forms.Select()
    valor = forms.DecimalField()
    data = forms.DateField(
        label='Data: ',
        required=False,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        input_formats=('%Y-%m-%d',),
    )
    observacao = forms.Textarea()
    valor_custo = forms.DecimalField()

    class Meta:
        model = OrdemServico
        fields = ('situacao','cliente','servico','valor','valor_custo','observacao')

    
