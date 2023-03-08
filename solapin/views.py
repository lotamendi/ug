from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from solapin.forms import SolapinForm
from solapin.mixins import ValidatePermissionRequiredMixin
from solapin.models import SolapinPersona
from config.settings import STATICFILES_DIRS

from PIL import Image, ImageDraw, ImageFont

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



class SolapinListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = SolapinPersona
    template_name = "list.html"
    permission_required = 'solapin.view_solapinpersona'
    url_redirect = 'solapin_dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Solapín'
        context['create_url'] = reverse_lazy('solapin_create')
        context['list_url'] = reverse_lazy('solapin_list')
        return context
    
class SolapinCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = SolapinPersona
    form_class = SolapinForm
    template_name = "create.html"
    success_url = reverse_lazy('solapin_list')
    permission_required = 'solapin.add_solapinpersona'
    url_redirect = 'solapin_dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva persona para solapín'
        context['list_url'] = reverse_lazy('solapin_list')
        context['action'] = 'add'
        return context
        
class SolapinUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = SolapinPersona
    template_name = "create.html"
    form_class = SolapinForm
    success_url = reverse_lazy('solapin_list')
    permission_required = 'solapin.change_solapinpersona'
    url_redirect = 'solapin_dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar persona para solapín'
        context['list_url'] = reverse_lazy('solapin_list')
        context['action'] = 'update'
        return context
    
class SolapinDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = SolapinPersona
    template_name = "delete.html"
    success_url = reverse_lazy('solapin_list')
    permission_required = 'solapin.delete_solapinpersona'
    url_redirect = 'solapin_dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar persona para solapín'
        context['list_url'] = reverse_lazy('solapin_list')
        return context

class SolapinGenerateView(TemplateView):
    template_name = "generate.html"
    image = Image.open('static/UG/img/solapin/diseno1_limpio.png')
    diseno_superior = False
    
    def dispatch(self, request, *args, **kwargs):
        # quiero obtener el id de la persona para obtener todos sus datos
        datos = {
            "no":3069,
            "nombre":"IDORKYS IRSULA MARTINEZ",
            "cargo":"SECRETARIA EJECUTIVA",
            "area_general":"Facultad de Ingenieria \ny Ciencias Tecnicas",
            "area_trabajo":"RECTORIA",
            "foto":'',
            'libre_acceso' : False,
            'diseno_superior': False
            }
        self.diseno_superior = datos['diseno_superior']
        if datos['diseno_superior'] == True:
            self.image = Image.open('static/UG/img/solapin/diseno2_limpio.png').convert('RGBA')
        else:
            self.image = Image.open('static/UG/img/solapin/diseno1_limpio.png').convert('RGBA')
        self.texto_area_general(datos['area_general'])
        self.texto_nombre(datos['nombre'])
        self.texto_cargo(datos['cargo'])
        self.texto_area_trabajo(datos['area_trabajo'])
        self.imagen_foto()
        if datos['libre_acceso']:
            self.texto_libre_acceso()
        self.image.show()
        # image.save("solapin/generate/test.jpg")
        return super().dispatch(request, *args, **kwargs)
        
    def texto_area_general(self, texto):

        draw = ImageDraw.Draw(self.image)
        if self.diseno_superior:
            font = ImageFont.truetype("static/UG/font/AGaramondPro-Bold.otf", 25)
            draw.multiline_text((33, 128), self.area_trabajo_cortada(str.upper(texto)) , font=font, fill="red")
        else:
            font = ImageFont.truetype("static/UG/font/AGaramondPro-Regular.otf", 25)
            draw.multiline_text((33, 128), self.area_trabajo_cortada(texto) , font=font, fill="white")
    
    def texto_nombre(self, texto):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("static/UG/font/Aller_Rg.ttf", 20)
        draw.multiline_text((36, 440), self.area_trabajo_cortada(str.title(texto)) , font=font, fill="black")
    
    def texto_cargo(self, texto):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("static/UG/font/Aller_Rg.ttf", 20)
        draw.multiline_text((36, 500), self.area_trabajo_cortada(str.title(texto)) , font=font, fill="black")
    
    def texto_area_trabajo(self, texto):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("static/UG/font/Aller_Rg.ttf", 20)
        draw.multiline_text((36, 565), self.area_trabajo_cortada(str.title(texto)) , font=font, fill="black")
    
    def texto_libre_acceso(self):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("static/UG/font/Aller_Rg.ttf", 40)
        draw.multiline_text((250, 200), self.area_trabajo_cortada('LIBRE \nACCESO') , font=font, fill="black", align="center")

    def imagen_foto(self):
        im1 = self.image
        im2 = Image.open('media/solapin/3254/IMG_2242.JPG').resize((174,186))
        mask_im = Image.new("1", im2.size, 0)
        draw = ImageDraw.Draw(mask_im)
        draw.rectangle((0, 0, 354, 354), fill=255)
        im1.paste(im2,(22,203), mask_im)

    def area_trabajo_cortada(self, nombre):
        # IMPLEMENTAR
        # limita la cantidad de caracteres e inserta un salto de linea
        # temp = nombre[:30]
        # "Facultad de Ingenieria \ny Ciencias Tecnicas"
        return nombre