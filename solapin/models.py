import os
from django.db import models
from config.settings import MEDIA_URL

def user_directory_path(instance, filename):
    return 'solapin/{0}/{1}'.format(instance.no, filename)

class SolapinPersona(models.Model):
    no = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    area_general = models.CharField(max_length=255)
    area_trabajo = models.CharField(max_length=255)
    foto = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'solapin_persona'

    def get_image(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(MEDIA_URL, 'solapin/sin_foto.jpg')
    