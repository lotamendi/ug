from django.contrib import admin
# from posgrado.models import *
from posgrado.models.clasif import *
from posgrado.models.models import Posgrado, Persona, Matricula, Certificado

# Clasificadores
admin.site.register(Facultad)
admin.site.register(FormaPosgrado)
admin.site.register(Organismo)
admin.site.register(Pais)
admin.site.register(Programa)

# Modelos de trabajo normal
admin.site.register(Posgrado)
admin.site.register(Persona)
admin.site.register(Matricula)
admin.site.register(Certificado)