from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

class foundationViews (TemplateView):
    template_name='home/foundation.html'

class indexViews (TemplateView):
    template_name='home.html'
    
class indexViews (TemplateView):
    template_name='home.html'

# Create your views here.


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = 'home/prueba_list.html'
    context_object_name = 'lita_prueba' 

class PruebaCreateView(CreateView):
    model = Prueba                   
    form_class = PruebaForm          
    template_name = 'home/addd.html'
    success_url = '/'
