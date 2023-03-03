from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, SimpleDocTemplate, Spacer, TableStyle

from reportlab.lib import colors

from posgrado.models.models import Matricula, Posgrado


class Reporte_PG14_View(TemplateView):
    template_name = "reportes/pg14.html"
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'filtrar_posgrado':
                data = []
                estudiantes = Matricula.objects.filter(posgrado=request.POST['id'])
                for i in estudiantes:
                    data.append({
                        'nombre':i.persona.nombre, 
                        'ap1': i.persona.apellido1,
                        'ap2': i.persona.apellido2,
                        'eval': 'evaluacion'
                        })
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'PG14: Acta de evaluación para las actividades de posgrado'
        context['data'] = {
            'posgrados': Posgrado.objects.all()
        }
        return context
    


def GenPDF(tablename):
    elements = []
    response = HttpResponse(content_type="application/octet-stream")
    response["Content-Disposition"] = 'attachment;filename="test.pdf"'

    doc = SimpleDocTemplate(response)
    elements.append(Spacer(1, 12))

    

    data=  [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    t=Table(data, None, None, TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
    elements.append(t)
    doc.build(elements)

    return response