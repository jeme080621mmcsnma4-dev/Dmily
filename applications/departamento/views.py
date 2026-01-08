#from django.shortcuts import render
from django.views.generic.edit import FormView


from .models import Departamento
from applications.personas.models import Empleado   
from .forms import NewDepartamentoForms

from django.views.generic import (ListView)


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name='departamentos'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForms
    success_url = '/'

    def form_valid(self, form):
        Departamento.objects.create(
            nombre=form.cleaned_data['nombre'],
            subnombre=form.cleaned_data['short_name']
        )
        return super().form_valid(form)
