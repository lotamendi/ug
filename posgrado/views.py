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
    
# Clasificadores
#  Facultad
class FacultadListView(LoginRequiredMixin, ListView):
    model = Facultad
    template_name = "clasificadores/facultad/list.html"
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Clasificador de facultades'
        context['create_url'] = reverse_lazy('facultad_create')
        context['list_url'] = reverse_lazy('facultad_list')
        context['entity'] = 'Facultad'
        return context
class FacultadCreateView(CreateView):
    model = Facultad
    form_class = C_FacultadForm
    template_name = "clasificadores/facultad/create.html"
    success_url = reverse_lazy('facultad_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva facultad'
        context['entity'] = 'Facultad'
        context['list_url'] = reverse_lazy('facultad_list')
        context['action'] = 'add'
        return context
class FacultadUpdateView(UpdateView):
    model = Facultad
    form_class = C_FacultadForm
    template_name = "clasificadores/facultad/create.html"
    success_url = reverse_lazy('facultad_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar facultad'
        context['entity'] = 'Facultad'
        context['list_url'] = reverse_lazy('facultad_list')
        context['action'] = 'update'
        return context
class FacultadDeleteView(DeleteView):
    model = Facultad
    template_name = "clasificadores/facultad/delete.html"
    success_url = reverse_lazy('facultad_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar facultad'
        context['entity'] = 'Facultad'
        context['list_url'] = reverse_lazy('facultad_list')
        return context
#  Organismos
class OrganismoListView(ListView):
    model = Organismo
    template_name = "clasificadores/organismo/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Clasificador de organismos'
        context['create_url'] = reverse_lazy('organismo_create')
        context['list_url'] = reverse_lazy('organismo_list')
        context['entity'] = 'Organismo'
        return context
class OrganismoCreateView(CreateView):
    model = Organismo
    form_class = C_OrganismoForm
    template_name = "clasificadores/organismo/create.html"
    success_url = reverse_lazy('organismo_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo organismo'
        context['entity'] = 'Organismo'
        context['list_url'] = reverse_lazy('organismo_list')
        context['action'] = 'add'
        return context
class OrganismoUpdateView(UpdateView):
    model = Organismo
    form_class = C_OrganismoForm
    template_name = "clasificadores/organismo/create.html"
    success_url = reverse_lazy('organismo_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar organismo'
        context['entity'] = 'Organismo'
        context['list_url'] = reverse_lazy('organismo_list')
        context['action'] = 'update'
        return context
class OrganismoDeleteView(DeleteView):
    model = Organismo
    template_name = "clasificadores/organismo/delete.html"
    success_url = reverse_lazy('organismo_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar organismo'
        context['entity'] = 'Organismo'
        context['list_url'] = reverse_lazy('organismo_list')
        return context
#  Forma de posgrado
class FormaPosgradoListView(ListView):
    model = FormaPosgrado
    template_name = "clasificadores/forma_posgrado/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Clasificador de formas de posgrado'
        context['create_url'] = reverse_lazy('forma_posgrado_create')
        context['list_url'] = reverse_lazy('forma_posgrado_list')
        context['entity'] = 'Forma de posgrado'
        return context
class FormaPosgradoCreateView(CreateView):
    model = FormaPosgrado
    form_class = C_FormaPosgradoForm
    template_name = "clasificadores/forma_posgrado/create.html"
    success_url = reverse_lazy('forma_posgrado_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva forma de posgrado'
        context['entity'] = 'Forma de posgrado'
        context['list_url'] = reverse_lazy('forma_posgrado_list')
        context['action'] = 'add'
        return context
class FormaPosgradoUpdateView(UpdateView):
    model = FormaPosgrado
    form_class = C_FormaPosgradoForm
    template_name = "clasificadores/forma_posgrado/create.html"
    success_url = reverse_lazy('forma_posgrado_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar forma de posgrado'
        context['entity'] = 'Forma de posgrado'
        context['list_url'] = reverse_lazy('forma_posgrado_list')
        context['action'] = 'update'
        return context
class FormaPosgradoDeleteView(DeleteView):
    model = FormaPosgrado
    template_name = "clasificadores/forma_posgrado/delete.html"
    success_url = reverse_lazy('forma_posgrado_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar forma de posgrado'
        context['entity'] = 'Forma de posgrado'
        context['list_url'] = reverse_lazy('forma_posgrado_list')
        return context
#  Forma de posgrado
class PaisListView(ListView):
    model = Pais
    template_name = "clasificadores/pais/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Clasificador de paises'
        context['create_url'] = reverse_lazy('pais_create')
        context['list_url'] = reverse_lazy('pais_list')
        context['entity'] = 'País'
        return context
class PaisCreateView(CreateView):
    model = Pais
    form_class = C_PaisForm
    template_name = "clasificadores/pais/create.html"
    success_url = reverse_lazy('pais_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo país'
        context['entity'] = 'País'
        context['list_url'] = reverse_lazy('pais_list')
        context['action'] = 'add'
        return context
class PaisUpdateView(UpdateView):
    model = Pais
    form_class = C_PaisForm
    template_name = "clasificadores/pais/create.html"
    success_url = reverse_lazy('pais_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar país'
        context['entity'] = 'País'
        context['list_url'] = reverse_lazy('pais_list')
        context['action'] = 'update'
        return context
class PaisDeleteView(DeleteView):
    model = Pais
    template_name = "clasificadores/pais/delete.html"
    success_url = reverse_lazy('pais_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar país'
        context['entity'] = 'País'
        context['list_url'] = reverse_lazy('pais_list')
        return context
#  Forma de posgrado
class ProgramaListView(ListView):
    model = Programa
    template_name = "clasificadores/programa/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Clasificador de programas de posgrado'
        context['create_url'] = reverse_lazy('programa_create')
        context['list_url'] = reverse_lazy('programa_list')
        context['entity'] = 'Programa'
        return context
class ProgramaCreateView(CreateView):
    model = Programa
    form_class = C_ProgramaForm
    template_name = "clasificadores/programa/create.html"
    success_url = reverse_lazy('programa_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo programa'
        context['entity'] = 'Programa'
        context['list_url'] = reverse_lazy('programa_list')
        context['action'] = 'add'
        return context
class ProgramaUpdateView(UpdateView):
    model = Programa
    form_class = C_ProgramaForm
    template_name = "clasificadores/programa/create.html"
    success_url = reverse_lazy('programa_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar programa'
        context['entity'] = 'Programa'
        context['list_url'] = reverse_lazy('programa_list')
        context['action'] = 'update'
        return context
class ProgramaDeleteView(DeleteView):
    model = Programa
    template_name = "clasificadores/programa/delete.html"
    success_url = reverse_lazy('programa_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar programa'
        context['entity'] = 'Programa'
        context['list_url'] = reverse_lazy('programa_list')
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
