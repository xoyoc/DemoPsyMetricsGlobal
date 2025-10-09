from django.urls import path
from . import views

app_name = 'consultas'

urlpatterns = [
    path('', views.ConsultasView.as_view(), name='consultas'),
    path('mis-consultas/', views.MisConsultasView.as_view(), name='mis_consultas'),
    path('solicitar-consulta/', views.solicitar_consulta, name='solicitar_consulta'),
]
