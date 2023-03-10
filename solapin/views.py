import os
import base64
from io import BytesIO
import pathlib
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from PIL import Image, ImageDraw, ImageFont
from solapin.forms import SolapinForm
from solapin.mixins import ValidatePermissionRequiredMixin
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
    success_url = reverse_lazy('solapin_list')
    datos = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        output = BytesIO()
        rgb_img = self.image.convert('RGB')
        rgb_img.save(output, format="JPEG")
        image_data = base64.b64encode(output.getvalue())
        if not isinstance(image_data, str):
            # Python 3, decode from bytes to string
            image_data = image_data.decode()
        data_url = 'data:image/jpg;base64,' + image_data
        context["solapin_generado"] = data_url
        context['list_url'] = reverse_lazy('solapin_list')
        return context
    
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        self.guarda_fichero(request)
        return HttpResponseRedirect(self.success_url)
    
    def dispatch(self, request, *args, **kwargs):
        data = SolapinPersona.objects.get(pk=super().get_context_data(**kwargs)['pk'])
        self.datos = {
            "no":data.no,
            "nombre":data.nombre,
            "cargo":data.cargo,
            "area_general":data.area_general,
            "area_trabajo":data.area_trabajo,
            "foto":data.foto,
            'libre_acceso' : data.libre_acceso,
            'diseno_superior': data.diseno_superior
            }
        if self.datos['foto'] == '' or os.path.isfile(str(self.datos['foto'])):
            messages.add_message(request, messages.ERROR, '{} {}'.format('No se ha encontrado la foto en la ruta especificada.', self.datos['foto']))
            return redirect(self.success_url)
        self.generar_solapin(self.datos, request)
        return super().dispatch(request, *args, **kwargs)
        
    def generar_solapin(self, datos, request):
        self.diseno_superior = datos['diseno_superior']
        if datos['diseno_superior'] == True:
            self.image = Image.open('static/UG/img/solapin/diseno2_limpio.png').convert('RGBA')
        else:
            self.image = Image.open('static/UG/img/solapin/diseno1_limpio.png').convert('RGBA')
        self.texto_area_general(datos['area_general'])
        self.texto_normal(datos['nombre'], (36, 430))
        self.texto_normal(datos['cargo'], (36, 490))
        self.texto_normal(datos['area_trabajo'], (36, 555))
        self.imagen_foto(datos['foto'])
        self.firma_escaneada()
        if datos['libre_acceso']:
            self.texto_libre_acceso()

    def texto_area_general(self, texto):
        draw = ImageDraw.Draw(self.image)
        if self.diseno_superior:
            font = ImageFont.truetype("static/UG/font/AGaramondPro-Bold.otf", 25)
            draw.multiline_text((33, 125), self.cortar_texto(str.upper(texto), 30) , font=font, fill="red")
        else:
            font = ImageFont.truetype("static/UG/font/AGaramondPro-Regular.otf", 25)
            draw.multiline_text((33, 125), self.cortar_texto(texto, 30) , font=font, fill="white")
    
    def texto_normal(self, texto, coordenadas):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("static/UG/font/Aller_Rg.ttf", 20)
        draw.text(coordenadas, self.cortar_texto(str.title(texto),40) , font=font, fill="black")
    
    def texto_libre_acceso(self):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("static/UG/font/Aller_Rg.ttf", 40)
        draw.multiline_text((240, 200), self.cortar_texto('LIBRE \nACCESO', 20) , font=font, fill="black", align="center")

    def imagen_foto(self, ruta: str):
        im1 = self.image
        im2 = Image.open(ruta).resize((174,186))
        mask_im = Image.new("1", im2.size, 0)
        draw = ImageDraw.Draw(mask_im)
        draw.rectangle((0, 0, 354, 354), fill=255)
        im1.paste(im2,(22,203), mask_im)

    def firma_escaneada(self):
        im1 = self.image
        im2 = Image.open('static/UG/img/solapin/firma_RRHH.jpg').resize((152,62))
        mask_im = Image.new("1", im2.size, 0)
        draw = ImageDraw.Draw(mask_im)
        draw.rectangle((0, 0, 378, 340), fill=255)
        im1.paste(im2,(236,288), mask_im)

    def cortar_texto(self, texto: str, max_caracteres: int):
        salida = ''
        arreglo_palabras = texto.split(' ')
        linea = ''
        for palabra in arreglo_palabras:
            if len(linea) == 0:
                linea += palabra + ' '
            else:
                if len(linea)+len(palabra) < max_caracteres:
                    linea += palabra + ' '
                else:
                    salida += linea + '\n'
                    linea = palabra + ' '
        salida += linea
        return salida
    
    def guarda_fichero(self, request):
        titulo = '{}-{}.jpg'.format(self.datos['no'], self.datos['nombre']).replace(' ','_')
        rgb_img = self.image.convert('RGB')
        downloads_path = str(pathlib.Path.home() / "Downloads")
        rgb_img.save(os.path.join(downloads_path, titulo), format="JPEG")
        messages.add_message(request, messages.SUCCESS, '{} {}'.format('Solapín guardado satisfactoriamente.', titulo))
        
class SolapinGenerateAllView(TemplateView):
    template_name = "generateAll.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = reverse_lazy('solapin_list')
        context["solapines"] = SolapinPersona.objects.all().exclude(Q(foto__isnull = True) | Q(foto = ''))
        return context
    