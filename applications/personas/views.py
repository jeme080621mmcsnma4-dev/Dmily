from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView,
DetailView,
CreateView,
TemplateView,
UpdateView,
DeleteView)
from .models import Empleado
from .forms import EmpleadoForm 

class InicioView(TemplateView):
    template_name='persona/inicio.html'


class ListaEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by= 10
    ordering='first_name'
    context_object_name='empleados'
    model=Empleado

class lisAllEmpleados(ListView):
    paginate_by=4
    ordering='last_name'
    template_name = "persona/list.all.html" 

    def get_queryset(self):
        #print('**********************')
        palabra_clave = self.request.GET.get('kword', '') 
        #print('**********************', palabra)
        lista=Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista
    


class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['subnombre']
        lista=Empleado.objects.filter(
            departamento__subnombre__iexact=area
        )
        return lista


class ListEmpleadoByKword(ListView):
    model = Empleado                    
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'  

    def get_queryset(self):
        #print('**********************')
        palabra_clave = self.request.GET.get('kword', '') 
        #print('**********************', palabra)
        lista=Empleado.objects.filter(first_name=palabra_clave)
        return lista
    
class ListHabilidadesEmpleados(ListView):
    template_name='persona/habilidades.html'
    context_object_name='habilidades'

    def get_queryset(self):
        empleado=Empleado.objects.get(id=5)
        return empleado.habilidades.all()
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'
    context_object_name = 'empleado'


    def get_context_data(self, **kwargs):
        context=super(EmpleadoDetailView,self).get_context_data(**kwargs )
        context['titulo'] = 'Empleado del mes'
        return context
    
class SuccessView(TemplateView):
    template_name='persona/success.html'


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    success_url = reverse_lazy('persona_app:correcto')

    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super().form_valid(form)

    

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'persona/update.html'
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('persona_app:correcto')   

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**********************METHODO POST*************************')
        print(request.POST)
        print(request.POST['last_name'])

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('*******METODO FORM VALID*******')
        self.object = form.save()
        return super().form_valid(form) 
    
class EmpleadoDeleteView(DeleteView):
    model=Empleado
    template_name='persona/delate.html'
    success_url = reverse_lazy('persona_app:empleados_admin')   

