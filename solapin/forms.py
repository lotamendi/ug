from django.forms import ModelForm
from solapin.models import SolapinPersona

class SolapinForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        # self.fields['codigo'].widget.attrs['autofocus'] = True
    class Meta:
        model = SolapinPersona
        fields = '__all__'