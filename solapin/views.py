from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from solapin.forms import SolapinForm
from solapin.models import SolapinPersona

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