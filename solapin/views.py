from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from solapin.forms import SolapinForm
from solapin.models import SolapinPersona

class SolapinDashboardView(TemplateView):
    template_name = "solapin_dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Solapín'
        context["total_usuarios"] = SolapinPersona.objects.count()
        context["usuarios_sin_foto"] = SolapinPersona.objects.filter(Q(foto__isnull = True) | Q(foto = '')).count()
        context["usuarios_sin_foto_porciento"] = context['usuarios_sin_foto'] * 100 / context['total_usuarios']
        context["libre_acceso"] = SolapinPersona.objects.filter(libre_acceso = True).count()
        context["diseno_superior"] = SolapinPersona.objects.filter(diseno_superior = True).count()
        return context



class SolapinListView(LoginRequiredMixin, ListView):
    model = SolapinPersona
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Solapín'
        context['create_url'] = reverse_lazy('solapin_create')
        context['list_url'] = reverse_lazy('solapin_list')
        return context
class SolapinCreateView(CreateView):
    model = SolapinPersona
    form_class = SolapinForm
    template_name = "create.html"
    success_url = reverse_lazy('solapin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva persona para solapín'
        context['list_url'] = reverse_lazy('solapin_list')
        context['action'] = 'add'
        return context
        
class SolapinUpdateView(UpdateView):
    model = SolapinPersona
    template_name = "create.html"
    form_class = SolapinForm
    success_url = reverse_lazy('solapin_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar persona para solapín'
        context['list_url'] = reverse_lazy('solapin_list')
        context['action'] = 'update'
        return context
class SolapinDeleteView(DeleteView):
    model = SolapinPersona
    template_name = "delete.html"
    success_url = reverse_lazy('solapin_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar persona para solapín'
        context['list_url'] = reverse_lazy('solapin_list')
        return context