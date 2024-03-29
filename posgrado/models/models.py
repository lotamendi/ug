from django.db import models
from django.urls import reverse

from posgrado.models.clasif import Organismo, Pais, Programa, Facultad, FormaPosgrado
from posgrado.models.choices import *
from utils.number_to_roman import printRoman

class Posgrado(models.Model):
    nombre = models.CharField(max_length = 200, blank=False)
    edicion = models.IntegerField(default=1, verbose_name="Edición")
    codigo = models.ForeignKey(Programa, on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, blank=False, default=0)
    modalidad = models.CharField(max_length=15, choices=modalidad_choices)
    forma = models.ForeignKey(FormaPosgrado, on_delete=models.CASCADE, verbose_name='Forma de Posgrado', blank=False, default=0)
    cum = models.BooleanField(blank=False, verbose_name='Ejecutado en CUM')
    pais = models.BooleanField(blank=False, verbose_name='Ejecutado en otro pais')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de terminación')
    
    
    class Meta:
        verbose_name = "posgrado"
        verbose_name_plural = "posgrados"
        ordering = ['nombre']

    def __str__(self):
        # return self.nombre
        return f'{self.nombre}, {printRoman(self.edicion)} Edición'

class Persona(models.Model):
    CI = models.CharField(primary_key=True, max_length=11)
    nombre = models.CharField(max_length = 50, null=False)
    apellido1 = models.CharField(max_length = 50, null=False)
    apellido2 = models.CharField(max_length = 50, null=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="País")
    pasaporte = models.CharField(max_length = 20, null=True)
    sexo = models.CharField( max_length=10, choices=gender_choices, verbose_name='Sexo')
    domicilio = models.CharField(max_length=150, default='No definido')
    telefono = models.CharField(max_length = 20, null=True)
    correo = models.EmailField(max_length=50, null=True)
        

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"
        ordering = ['apellido1']

    def __str__(self):
        return self.nombre + ' ' + self.apellido1 + ' ' + self.apellido2

class Matricula(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE)
    posgrado = models.ForeignKey(Posgrado, on_delete=models.CASCADE)
    graduado = models.BooleanField(default=False)
    evaluacion = models.IntegerField(default=0, choices=evaluacion_choices, verbose_name='Evaluación')

    class Meta:
        verbose_name = "matricula"
        verbose_name_plural = "matriculas"
        ordering = ['id']

    def __str__(self):
        return self.persona.nombre

class Certificado(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    posgrado = models.ForeignKey(Posgrado, on_delete=models.CASCADE)
    emitido = models.CharField(max_length = 150)
    firmado = models.CharField(max_length = 150)
    
    class Meta:
        verbose_name = "certificado"
        verbose_name_plural = "certificados"

    def __str__(self):
        return self.name
