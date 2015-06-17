'''
from django import forms
from core.models import DistribuidorInterno

class DistribuirInternoForm(forms.ModelForm):
    model = DistribuidorInterno

    pessoa = forms.CharField(label='Teste') '''