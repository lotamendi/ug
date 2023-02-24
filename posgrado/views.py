from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from posgrado.models.clasif import *
from posgrado.models.models import *
from posgrado.forms import *

# Home
class DashboardView(TemplateView):
    template_name = "dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Inicio'
        context['data'] = {
            'posgrados': Posgrado.objects.count(),
            'personas': Persona.objects.count(),
            'matriculas' : Matricula.objects.count(),
            'certificados' : Certificado.objects.count()
        }
        return context
    
# Posgrado
class PosgradoListView(ListView):
    model = Posgrado
    template_name = "posgrado/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Programa de posgrado'
        context['create_url'] = reverse_lazy('posgrado_create')
        context['list_url'] = reverse_lazy('posgrado_list')
        context['entity'] = 'Posgrado'
        return context
class PosgradoCreateView(CreateView):
    model = Posgrado
    form_class = PosgradoForm
    template_name = "posgrado/create.html"
    success_url = reverse_lazy('posgrado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo programa de posgrado'
        context['entity'] = 'Posgrado'
        context['list_url'] = reverse_lazy('posgrado_list')
        context['action'] = 'add'
        return context
class PosgradoUpdateView(UpdateView):
    model = Posgrado
    template_name = "posgrado/create.html"
    form_class = PosgradoForm
    success_url = reverse_lazy('posgrado_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar programa de posgrado'
        context['entity'] = 'Posgrado'
        context['list_url'] = reverse_lazy('posgrado_list')
        context['action'] = 'update'
        return context
class PosgradoDeleteView(DeleteView):
    model = Posgrado
    template_name = "posgrado/delete.html"
    success_url = reverse_lazy('posgrado_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar programa de posgrado'
        context['entity'] = 'Posgrado'
        context['list_url'] = reverse_lazy('posgrado_list')
        return context

#Personas
class PersonaListView(ListView):
    model = Persona
    template_name = "persona/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Personas'
        context['create_url'] = reverse_lazy('persona_create')
        context['list_url'] = reverse_lazy('persona_list')
        context['entity'] = 'Personas'
        return context
class PersonaCreateView(CreateView):
    model = Persona
    template_name = "persona/create.html"
    form_class = PersonaForm
    success_url = reverse_lazy('persona_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva persona'
        context['entity'] = 'Personas'
        context['list_url'] = reverse_lazy('persona_list')
        context['action'] = 'add'
        return context
        
class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = "persona/create.html"
    form_class = PersonaForm
    success_url = reverse_lazy('persona_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar persona'
        context['entity'] = 'Personas'
        context['list_url'] = reverse_lazy('persona_list')
        context['action'] = 'update'
        return context
class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar persona'
        context['entity'] = 'Personas'
        context['list_url'] = reverse_lazy('persona_list')
        return context

# Matriculas
class MatriculaListView(ListView):
    model = Matricula
    template_name = "matricula/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Matrícula'
        context['create_url'] = reverse_lazy('matricula_create')
        context['list_url'] = reverse_lazy('matricula_list')
        context['entity'] = 'Matrículas'
        return context
class MatriculaCreateView(CreateView):
    model = Matricula
    template_name = "matricula/create.html"
    form_class = MatriculaForm
    success_url = reverse_lazy('matricula_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva matrícula'
        context['entity'] = 'Matrículas'
        context['list_url'] = reverse_lazy('matricula_list')
        context['action'] = 'add'
        return context
class MatriculaUpdateView(UpdateView):
    model = Matricula
    template_name = "matricula/create.html"
    form_class = MatriculaForm
    success_url = reverse_lazy('matricula_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar matrícula'
        context['entity'] = 'Matrículas'
        context['list_url'] = reverse_lazy('matricula_list')
        context['action'] = 'update'
        return context
class MatriculaDeleteView(DeleteView):
    model = Matricula
    template_name = "matricula/delete.html"
    success_url = reverse_lazy('matricula_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar matrícula'
        context['entity'] = 'Matrículas'
        context['list_url'] = reverse_lazy('matricula_list')
        return context
