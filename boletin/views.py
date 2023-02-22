from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'Boletín UG'
        context["title"] = 'Boletín estadístico' #Boletín estadístico, Universidad de Guantánamo
        context["subtitle"] = 'Universidad de Guantánamo' # Este boletín proporciona información estadística detallada sobre la estructura, personal y principales indicadores de actividad en los ámbitos de docencia, investigación y extensión universitaria.'
        context["company"] = 'Universidad de Guantánamo'
        context["contact"] = {
          'location': 'Avenida Che Guevara. Km 1/2. Carretera a Jamaica, Guantánamo, Cuba. CP:95100',
          'phone': '+53 21326113',
          'email': 'dcomunicacion@cug.co.cu'
        }
        context['data'] = {
          'estudiantes' : {
            'total': 500,
            'hombres': 15,
            'mujeres':45
          },
          'profesores' : {
            'total': 500,
            'sexo' : {
              'hombres': 15,
              'mujeres':45
            },
            'categoria' : {
              'licenciado' : 0,
              'master' : 0,
              'doctor' : 0,
              'instructor' : 0,
              'asistente' : 0,
              'auxiliar' : 0,
              'titular' : 0
            }
          },
          'cursos' : {
            'regular_diurno' : 15,
            'por_encuentro' : 5,
            'a_distancia' : 45,
          },
          'org_masa' : {
            'ujc' : 45,
            'pcc' : 7
          },
          'otros' : {
            'convenios_internac' : 15,
            'carreras_acreditadas' : 95,
            'becas_internac' : 45,
          }
        }
        return context
    