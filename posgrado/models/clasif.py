from django.db import models

# Clasificador de facultades
class Facultad(models.Model):
    nombre = models.CharField(max_length = 150)
    abrev = models.CharField(max_length = 20, blank = False)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "_Facultad"
        verbose_name_plural = "_Facultades"
        db_table = 'clas_facultad'
        ordering = ['id']

    def __str__(self):
        return self.nombre + ' (' + self.abrev + ')'

# Clasificador de Organismos
class Organismo(models.Model):
    nombre = models.CharField(max_length = 150)
    sigla = models.CharField(max_length = 20)
    
    class Meta:
        verbose_name = "_Organismo"
        verbose_name_plural = "_Organismos"
        db_table = 'clas_organismo'
        ordering = ['id']

    def __str__(self):
        return self.nombre + ' (' + self.sigla + ')'

# Clasificador de formas de posgrado
class FormaPosgrado(models.Model):
    nombre = models.CharField(max_length = 150)
    abrev = models.CharField(max_length = 20)

    class Meta:
        verbose_name = "_Forma de Posgrado"
        verbose_name_plural = "_Formas de Posgrado"
        db_table = 'clas_formaPosgrado'
        ordering = ['id']

    def __str__(self):
        return self.nombre + ' (' + self.abrev + ')'

# Clasificador de Paises
class Pais(models.Model):
    nombre = models.CharField(max_length = 100)
    sigla = models.CharField(max_length = 3)
    area = models.CharField(max_length = 30)

    class Meta:
        verbose_name = "_Pais"
        verbose_name_plural = "_Paises"
        db_table = 'clas_pais'
        ordering = ['nombre']

    def __str__(self):
        return self.sigla + ' - ' + self.nombre

# Clasificador de programas (Maestria y Especialidades)
class Programa(models.Model):
    codigo = models.CharField(max_length = 11, primary_key=True)
    rama = models.CharField(max_length = 150, blank=False)
    tipo = models.CharField(max_length = 10, blank=False)

    class Meta:
        verbose_name = "_Programa"
        verbose_name_plural = "_Programas"
        db_table = 'clas_programa'
        ordering = ['codigo']

    def __str__(self):
        return self.codigo + ' - ' + self.rama
