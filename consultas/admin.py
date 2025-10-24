from django.contrib import admin
from .models import (
    TipoConsulta,
    Psicologo,
    Consulta,
    DisponibilidadPsicologo,
    MensajeConsulta
)


# Inlines para Consultas
class DisponibilidadPsicologoInline(admin.TabularInline):
    """Inline para agregar disponibilidad al psicólogo"""
    model = DisponibilidadPsicologo
    extra = 2
    fields = ['dia_semana', 'hora_inicio', 'hora_fin', 'activo']
    ordering = ['dia_semana', 'hora_inicio']


class MensajeConsultaInline(admin.StackedInline):
    """Inline para ver mensajes de una consulta"""
    model = MensajeConsulta
    extra = 0
    fields = ['remitente', 'mensaje', 'leido', 'fecha_envio']
    readonly_fields = ['fecha_envio']
    ordering = ['fecha_envio']


# Admin para Tipos de Consulta
@admin.register(TipoConsulta)
class TipoConsultaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'duracion_minutos', 'precio', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre', 'descripcion']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Detalles', {
            'fields': ('duracion_minutos', 'precio', 'activo')
        }),
    )


# Admin para Psicólogos
@admin.register(Psicologo)
class PsicologoAdmin(admin.ModelAdmin):
    list_display = ['get_nombre_completo', 'especialidad', 'experiencia_anos', 'tarifa_hora', 'disponible']
    list_filter = ['especialidad', 'disponible', 'experiencia_anos']
    search_fields = ['usuario__username', 'usuario__first_name', 'usuario__last_name', 'descripcion']
    inlines = [DisponibilidadPsicologoInline]
    
    fieldsets = (
        ('Información del Psicólogo', {
            'fields': ('usuario', 'especialidad', 'experiencia_anos')
        }),
        ('Descripción y Tarifa', {
            'fields': ('descripcion', 'tarifa_hora')
        }),
        ('Estado y Multimedia', {
            'fields': ('disponible', 'foto')
        }),
    )
    
    def get_nombre_completo(self, obj):
        """Muestra el nombre completo del psicólogo"""
        return f"Dr./Dra. {obj.usuario.get_full_name() or obj.usuario.username}"
    get_nombre_completo.short_description = 'Psicólogo'
    get_nombre_completo.admin_order_field = 'usuario__first_name'


# Admin para Consultas
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['get_cliente_nombre', 'get_psicologo_nombre', 'tipo_consulta', 'estado', 'fecha_agendada', 'calificacion']
    list_filter = ['estado', 'fecha_solicitud', 'fecha_agendada', 'tipo_consulta']
    search_fields = ['cliente__username', 'cliente__first_name', 'psicologo__usuario__first_name', 'motivo_consulta']
    readonly_fields = ['fecha_solicitud']
    inlines = [MensajeConsultaInline]
    date_hierarchy = 'fecha_agendada'
    
    fieldsets = (
        ('Información de la Consulta', {
            'fields': ('cliente', 'psicologo', 'tipo_consulta')
        }),
        ('Fechas y Duración', {
            'fields': ('fecha_solicitud', 'fecha_agendada', 'duracion_minutos')
        }),
        ('Estado y Motivo', {
            'fields': ('estado', 'motivo_consulta')
        }),
        ('Notas', {
            'fields': ('notas_cliente', 'notas_psicologo'),
            'classes': ('collapse',)  # Colapsable por defecto
        }),
        ('Calificación y Comentarios', {
            'fields': ('calificacion', 'comentarios_finales'),
            'classes': ('collapse',)
        }),
    )
    
    def get_cliente_nombre(self, obj):
        """Muestra el nombre del cliente"""
        return obj.cliente.get_full_name() or obj.cliente.username
    get_cliente_nombre.short_description = 'Cliente'
    get_cliente_nombre.admin_order_field = 'cliente__first_name'
    
    def get_psicologo_nombre(self, obj):
        """Muestra el nombre del psicólogo"""
        return obj.psicologo.usuario.get_full_name() or obj.psicologo.usuario.username
    get_psicologo_nombre.short_description = 'Psicólogo'
    get_psicologo_nombre.admin_order_field = 'psicologo__usuario__first_name'


# Admin para Disponibilidad de Psicólogos
@admin.register(DisponibilidadPsicologo)
class DisponibilidadPsicologoAdmin(admin.ModelAdmin):
    list_display = ['psicologo', 'get_dia_nombre', 'hora_inicio', 'hora_fin', 'activo']
    list_filter = ['dia_semana', 'activo', 'psicologo']
    search_fields = ['psicologo__usuario__username', 'psicologo__usuario__first_name']
    ordering = ['psicologo', 'dia_semana', 'hora_inicio']
    
    fieldsets = (
        (None, {
            'fields': ('psicologo', 'dia_semana', 'hora_inicio', 'hora_fin', 'activo')
        }),
    )
    
    def get_dia_nombre(self, obj):
        """Muestra el nombre del día de la semana"""
        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        return dias[obj.dia_semana]
    get_dia_nombre.short_description = 'Día'
    get_dia_nombre.admin_order_field = 'dia_semana'


# Admin para Mensajes de Consulta
@admin.register(MensajeConsulta)
class MensajeConsultaAdmin(admin.ModelAdmin):
    list_display = ['consulta', 'remitente', 'get_mensaje_corto', 'leido', 'fecha_envio']
    list_filter = ['leido', 'fecha_envio']
    search_fields = ['mensaje', 'remitente__username', 'consulta__cliente__username']
    readonly_fields = ['fecha_envio']
    date_hierarchy = 'fecha_envio'
    
    fieldsets = (
        (None, {
            'fields': ('consulta', 'remitente')
        }),
        ('Mensaje', {
            'fields': ('mensaje', 'leido', 'fecha_envio')
        }),
    )
    
    def get_mensaje_corto(self, obj):
        """Muestra una versión corta del mensaje"""
        return obj.mensaje[:50] + '...' if len(obj.mensaje) > 50 else obj.mensaje
    get_mensaje_corto.short_description = 'Mensaje'
