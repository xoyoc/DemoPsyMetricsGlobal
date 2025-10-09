from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ConsultasView(TemplateView):
    template_name = 'consultas/consultas.html'


@method_decorator(login_required, name='dispatch')
class MisConsultasView(TemplateView):
    template_name = 'consultas/mis_consultas.html'


def solicitar_consulta(request):
    if request.method == 'POST':
        return JsonResponse({'success': True, 'message': 'Consulta solicitada correctamente'})
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})