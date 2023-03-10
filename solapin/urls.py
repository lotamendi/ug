from django.urls import path
from solapin.views import *

urlpatterns = [
    path('', SolapinDashboardView.as_view(), name='solapin_dashboard'),
    # CRUD
    path('list/', SolapinListView.as_view(), name='solapin_list'),
    path('add/', SolapinCreateView.as_view(), name='solapin_create'),
    path('update/<int:pk>/', SolapinUpdateView.as_view(), name='solapin_update'),
    path('delete/<int:pk>/', SolapinDeleteView.as_view(), name='solapin_delete'),
    # Otras funciones
    path('generate/<int:pk>/', SolapinGenerateView.as_view(), name='solapin_generate'),
    path('generateAll', SolapinGenerateAllView.as_view(), name='solapin_generate_all')
]
