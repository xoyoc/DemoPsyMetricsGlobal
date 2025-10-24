from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
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


def logout_view(request):
    """Vista personalizada de logout que redirige al home"""
    logout(request)
    return redirect('evaluaciones:home')


def login_view(request):
    """Vista personalizada de login"""
    if request.user.is_authenticated:
        return redirect('evaluaciones:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.first_name or user.username}!')
            
            # Redirigir a la página que intentaba acceder o al dashboard
            next_url = request.GET.get('next', 'evaluaciones:dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'auth/login.html')


def register_view(request):
    """Vista personalizada de registro"""
    if request.user.is_authenticated:
        return redirect('evaluaciones:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validaciones
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif len(password1) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
        else:
            # Crear usuario
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
            
            # Login automático después del registro
            login(request, user)
            messages.success(request, f'¡Bienvenido, {first_name}! Tu cuenta ha sido creada exitosamente.')
            return redirect('evaluaciones:dashboard')
    
    return render(request, 'auth/register.html')
