import os
from django.db import models
from config.settings import MEDIA_URL

def user_directory_path(instance, filename):
    return 'solapin/{0}/{1}'.format(instance.no, filename)

class SolapinPersona(models.Model):
    no = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name='Nombre y apellidos')
    cargo = models.CharField(max_length=255)
    area_general = models.CharField(max_length=255, verbose_name='Área general')
    area_trabajo = models.CharField(max_length=255, verbose_name='Área de trabajo')
    foto = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    libre_acceso = models.BooleanField(default=False)
    diseno_superior = models.BooleanField(default=False, verbose_name='Diseño superior (Solo para Rectoría y Vicerrectoría)')

    class Meta:
        db_table = 'solapin_persona'

    def get_image(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(MEDIA_URL, 'solapin/sin_foto.jpg')
    