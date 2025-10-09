from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estadisticas'] = {
            'evaluaciones_realizadas': 500,
            'clientes_corporativos': 200,
            'tasa_exito': 95,
        }
        return context


class ServiciosView(TemplateView):
    template_name = 'servicios.html'


class NosotrosView(TemplateView):
    template_name = 'nosotros.html'


class ContactoView(TemplateView):
    template_name = 'contacto.html'


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard.html'


def solicitar_evaluacion(request):
    if request.method == 'POST':
        return JsonResponse({'success': True, 'message': 'Solicitud enviada correctamente'})
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})