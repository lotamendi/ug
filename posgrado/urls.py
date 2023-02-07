from django.urls import include, path
from posgrado.views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    # Clasificadores
    path('clasificadores/', include('posgrado.templates.clasificadores.urls')),
    # Modelos
    path('posgrado/list/', PosgradoListView.as_view(), name='posgrado_list'),
    path('posgrado/add/', PosgradoCreateView.as_view(), name='posgrado_create'),
    path('posgrado/update/<int:pk>/', PosgradoUpdateView.as_view(), name='posgrado_update'),
    path('posgrado/delete/<int:pk>/', PosgradoDeleteView.as_view(), name='posgrado_delete'),
    path('persona/list/', PersonaListView.as_view(), name='persona_list'),
    path('persona/add/', PersonaCreateView.as_view(), name='persona_create'),
    path('persona/update/<int:pk>/', PersonaUpdateView.as_view(), name='persona_update'),
    path('persona/delete/<int:pk>/', PersonaDeleteView.as_view(), name='persona_delete'),
    path('matricula/list/', MatriculaListView.as_view(), name='matricula_list'),
    path('matricula/add/', MatriculaCreateView.as_view(), name='matricula_create'),
    path('matricula/update/<int:pk>/', MatriculaUpdateView.as_view(), name='matricula_update'),
    path('matricula/delete/<int:pk>/', MatriculaDeleteView.as_view(), name='matricula_delete'),
]