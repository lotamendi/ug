from django.urls import path
from posgrado.templates.clasificadores.views import *

urlpatterns = [
    path('facultad/list/', FacultadListView.as_view(), name='facultad_list'),
    path('facultad/add/', FacultadCreateView.as_view(), name='facultad_create'),
    path('facultad/update/<int:pk>/', FacultadUpdateView.as_view(), name='facultad_update'),
    path('facultad/active/<int:pk>/', FacultadActiveView.as_view(), name='facultad_active'),
    path('facultad/delete/<int:pk>/', FacultadDeleteView.as_view(), name='facultad_delete'),
    path('organismo/list/', OrganismoListView.as_view(), name='organismo_list'),
    path('organismo/add/', OrganismoCreateView.as_view(), name='organismo_create'),
    path('organismo/update/<int:pk>/', OrganismoUpdateView.as_view(), name='organismo_update'),
    path('organismo/delete/<int:pk>/', OrganismoDeleteView.as_view(), name='organismo_delete'),
    path('forma_posgrado/list/', FormaPosgradoListView.as_view(), name='forma_posgrado_list'),
    path('forma_posgrado/add/', FormaPosgradoCreateView.as_view(), name='forma_posgrado_create'),
    path('forma_posgrado/update/<int:pk>/', FormaPosgradoUpdateView.as_view(), name='forma_posgrado_update'),
    path('forma_posgrado/delete/<int:pk>/', FormaPosgradoDeleteView.as_view(), name='forma_posgrado_delete'),
    path('pais/list/', PaisListView.as_view(), name='pais_list'),
    path('pais/add/', PaisCreateView.as_view(), name='pais_create'),
    path('pais/update/<int:pk>/', PaisUpdateView.as_view(), name='pais_update'),
    path('pais/delete/<int:pk>/', PaisDeleteView.as_view(), name='pais_delete'),
    path('programa/list/', ProgramaListView.as_view(), name='programa_list'),
    path('programa/add/', ProgramaCreateView.as_view(), name='programa_create'),
    path('programa/update/<int:pk>/', ProgramaUpdateView.as_view(), name='programa_update'),
    path('programa/delete/<int:pk>/', ProgramaDeleteView.as_view(), name='programa_delete'),
]