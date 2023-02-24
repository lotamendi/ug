from datetime import datetime
from django.forms import ModelForm, TextInput, Textarea
from posgrado.models.clasif import *
from posgrado.models.models import Matricula, Persona, Posgrado


class C_FacultadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = Facultad
        fields = '__all__'
        exclude = ['activo']
class C_OrganismoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = Organismo
        fields = '__all__'
class C_FormaPosgradoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = FormaPosgrado
        fields = '__all__'
class C_PaisForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = Pais
        fields = '__all__'
class C_ProgramaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['codigo'].widget.attrs['autofocus'] = True
        # print(self.) Aqui debe deshabilitar el campo codigo 
        # cuando el action es update
    class Meta:
        model = Programa
        fields = '__all__'

class PosgradoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'form-control'})
            # form.field.widget.attrs['class'] = 'form-control' # form-control-border
        self.fields['nombre'].widget.attrs['autofocus'] = True
        self.fields['facultad'].queryset = Facultad.objects.filter(activo=1)
    class Meta:
        model = Posgrado
        fields = '__all__'
        exclude = ['fecha_fin']
        widgets = {
            'fecha_inicio' : TextInput(
                attrs={
                    'type' : 'date',
                    'value' : datetime.now().strftime('%Y-%m-%d')
                }
            )
        #     'nombre' : TextInput(
        #         attrs={
        #             'placeholder':'Escriba un nombre',
        #         }
        #     )
        }

class PersonaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['CI'].widget.attrs['autofocus'] = True
    class Meta:
        model = Persona
        fields = "__all__"

class MatriculaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Matricula
        fields = "__all__"
