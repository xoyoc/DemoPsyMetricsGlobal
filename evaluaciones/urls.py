from django.urls import path
from . import views

app_name = 'evaluaciones'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('servicios/', views.ServiciosView.as_view(), name='servicios'),
    path('nosotros/', views.NosotrosView.as_view(), name='nosotros'),
    path('contacto/', views.ContactoView.as_view(), name='contacto'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('solicitar-evaluacion/', views.solicitar_evaluacion, name='solicitar_evaluacion'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
