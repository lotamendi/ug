from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, SimpleDocTemplate, Spacer, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

from posgrado.models.models import Matricula, Posgrado
from posgrado.models.choices import evaluacion_choices

# from utils.testing_reportlab import generate
from io import BytesIO
from reportlab.lib.pagesizes import letter, landscape, A4



class Reporte_PG14_View(TemplateView):
    template_name = "reportes/pg14.html"
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            print(request.POST)
            action = request.POST['action']
            if action == 'filtrar_posgrado':
                data = rellena_data(request.POST['id'])
            # elif action == 'generate_report':
            #     data_estudiantes = self.rellena_data(request.POST['id'])
            #     data_posgrado = Posgrado.objects.filter(id=request.POST['id'])
            #     # De aqui obtengo:
            #     # Programa: nombre
            #     # Edicion: edicion
            #     # Actividad:
            #     # Creditos:
            #     # Profesor:
            #     # Coordinador:
            #     return GenPDF()
                
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

def rellena_data(id):
    data = []
    estudiantes = Matricula.objects.filter(posgrado=id).order_by('persona')
    cont = 0
    for i in estudiantes:
        cont = cont + 1
        data.append({
            'no':cont, 
            'nombre': f"{i.persona.apellido1} {i.persona.apellido2}, {i.persona.nombre}", 
            'eval':  evaluacion_choices[i.evaluacion][1]
            })
    return data
# def GenPDF():
#     response = HttpResponse(content_type="application/pdf")
#     response["Content-Disposition"] = 'attachment;filename="test.pdf"'

#     p = canvas.Canvas(response)
#     p.setFont("Courier", 28)
#     p.drawString(60, 750, "Hola mundo")
#     p.showPage()
#     p.save()
    # Story = []
    # Story.append(Spacer(1, 12))

    # data=  [['00', '01', '02', '03', '04'],
    #         ['10', '11', '12', '13', '14'],
    #         ['20', '21', '22', '23', '24'],
    #         ['30', '31', '32', '33', '34']]
    # t=Table(data, None, None, TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
    # Story.append(t)
    
    # doc = SimpleDocTemplate(response)
    # doc.build(Story)
    # return response

def generate_pdf(request, id):
    response = HttpResponse(content_type='application/pdf')
    response["Content-Disposition"] = 'inline;filename="test.pdf"'
    
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    #Datos a imprimir
    data_estudiantes = rellena_data(id)
    data_posgrado = Posgrado.objects.filter(id=id)
    # De aqui obtengo:
    # Programa: nombre
    # Edicion: edicion
    # Actividad:
    # Creditos:
    # Profesor:
    # Coordinador:


    # Inicia a dibujar el PDF
    data = [
        ["PG-14", 'UNIVERSIDAD DE GUANTÁNAMO\nACTA DE EVALUACIÓN PARA LAS ACTIVIDADECS DE POSGRADO'],
        [f"Programa: {data_posgrado[0].nombre}", f"Edición: {data_posgrado[0].edicion}"],
        ["Actividad: "],
        ["Créditos: "],
        ["No.", "APELLIDOS Y NOMBRES", "EVALUACIÓN"]
    ]
    t = Table(data)
    t.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,0), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black)
    ]))
    t.wrapOn(p,400,100)
    t.drawOn(p,100,600)
    # p.setFont("Helvetica", 15, leading=None)
    # p.setFillColorRGB(0.29296875, 0.453125, 0.609375)
    # p.drawString(260, 800, "Hola mundo")
    # p.line(0,780,1000,780)
    p.setTitle('Reporte')

    # Renderizar el documento
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response