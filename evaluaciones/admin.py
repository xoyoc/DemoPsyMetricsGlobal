from django.contrib import admin
from .models import (
    CuestionarioNOM035,
    DominioNOM035,
    PreguntaNOM035,
    OpcionRespuesta,
    Evaluacion,
    RespuestaEvaluacion,
    TipoEvaluacion,
    EvaluacionPersonalizada
)


# Inlines para estructura jerárquica
class OpcionRespuestaInline(admin.TabularInline):
    """Inline para agregar opciones de respuesta a las preguntas"""
    model = OpcionRespuesta
    extra = 4
    fields = ['texto', 'valor', 'orden']
    ordering = ['orden']


class PreguntaNOM035Inline(admin.StackedInline):
    """Inline para agregar preguntas a los dominios"""
    model = PreguntaNOM035
    extra = 1
    fields = ['texto', 'tipo', 'orden', 'obligatoria']
    ordering = ['orden']
    show_change_link = True  # Permite editar la pregunta en su propia página


class DominioNOM035Inline(admin.StackedInline):
    """Inline para agregar dominios a los cuestionarios"""
    model = DominioNOM035
    extra = 1
    fields = ['nombre', 'descripcion', 'orden']
    ordering = ['orden']
    show_change_link = True


class RespuestaEvaluacionInline(admin.TabularInline):
    """Inline para ver respuestas de una evaluación"""
    model = RespuestaEvaluacion
    extra = 0
    fields = ['pregunta', 'opcion_seleccionada', 'respuesta_texto', 'puntuacion', 'fecha_respuesta']
    readonly_fields = ['fecha_respuesta']
    can_delete = False


# Admin para Cuestionarios
@admin.register(CuestionarioNOM035)
class CuestionarioNOM035Admin(admin.ModelAdmin):
    list_display = ['nombre', 'version', 'estado', 'creado_por', 'fecha_creacion']
    list_filter = ['estado', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion', 'version']
    readonly_fields = ['fecha_creacion']
    inlines = [DominioNOM035Inline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'version', 'descripcion')
        }),
        ('Estado y Control', {
            'fields': ('estado', 'creado_por', 'fecha_creacion')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Asigna automáticamente el usuario que crea el cuestionario"""
        if not change:  # Si es un nuevo objeto
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)


# Admin para Dominios
@admin.register(DominioNOM035)
class DominioNOM035Admin(admin.ModelAdmin):
    list_display = ['nombre', 'cuestionario', 'orden', 'get_num_preguntas']
    list_filter = ['cuestionario']
    search_fields = ['nombre', 'descripcion']
    inlines = [PreguntaNOM035Inline]
    ordering = ['cuestionario', 'orden']
    
    fieldsets = (
        (None, {
            'fields': ('cuestionario', 'nombre', 'descripcion', 'orden')
        }),
    )
    
    def get_num_preguntas(self, obj):
        """Muestra el número de preguntas en el dominio"""
        return obj.preguntanom035_set.count()
    get_num_preguntas.short_description = 'Nº Preguntas'


# Admin para Preguntas
@admin.register(PreguntaNOM035)
class PreguntaNOM035Admin(admin.ModelAdmin):
    list_display = ['get_pregunta_corta', 'dominio', 'tipo', 'orden', 'obligatoria', 'get_num_opciones']
    list_filter = ['tipo', 'obligatoria', 'dominio__cuestionario']
    search_fields = ['texto']
    inlines = [OpcionRespuestaInline]
    ordering = ['dominio', 'orden']
    
    fieldsets = (
        (None, {
            'fields': ('dominio', 'texto', 'tipo', 'orden', 'obligatoria')
        }),
    )
    
    def get_pregunta_corta(self, obj):
        """Muestra una versión corta del texto de la pregunta"""
        return obj.texto[:50] + '...' if len(obj.texto) > 50 else obj.texto
    get_pregunta_corta.short_description = 'Pregunta'
    
    def get_num_opciones(self, obj):
        """Muestra el número de opciones de respuesta"""
        return obj.opcionrespuesta_set.count()
    get_num_opciones.short_description = 'Nº Opciones'


# Admin para Opciones de Respuesta
@admin.register(OpcionRespuesta)
class OpcionRespuestaAdmin(admin.ModelAdmin):
    list_display = ['texto', 'pregunta', 'valor', 'orden']
    list_filter = ['pregunta__dominio__cuestionario']
    search_fields = ['texto', 'pregunta__texto']
    ordering = ['pregunta', 'orden']
    
    fieldsets = (
        (None, {
            'fields': ('pregunta', 'texto', 'valor', 'orden')
        }),
    )


# Admin para Evaluaciones
@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ['get_evaluado_nombre', 'cuestionario', 'estado', 'fecha_inicio', 'puntuacion_total']
    list_filter = ['estado', 'fecha_inicio', 'cuestionario']
    search_fields = ['evaluado__username', 'evaluado__first_name', 'evaluado__last_name']
    readonly_fields = ['fecha_inicio', 'fecha_completado']
    inlines = [RespuestaEvaluacionInline]
    
    fieldsets = (
        ('Información de la Evaluación', {
            'fields': ('cuestionario', 'evaluado', 'evaluador')
        }),
        ('Estado y Progreso', {
            'fields': ('estado', 'puntuacion_total', 'fecha_inicio', 'fecha_completado')
        }),
    )
    
    def get_evaluado_nombre(self, obj):
        """Muestra el nombre completo del evaluado"""
        return obj.evaluado.get_full_name() or obj.evaluado.username
    get_evaluado_nombre.short_description = 'Evaluado'
    get_evaluado_nombre.admin_order_field = 'evaluado__first_name'


# Admin para Respuestas de Evaluación
@admin.register(RespuestaEvaluacion)
class RespuestaEvaluacionAdmin(admin.ModelAdmin):
    list_display = ['evaluacion', 'pregunta', 'opcion_seleccionada', 'puntuacion', 'fecha_respuesta']
    list_filter = ['evaluacion__estado', 'fecha_respuesta']
    search_fields = ['evaluacion__evaluado__username', 'pregunta__texto']
    readonly_fields = ['fecha_respuesta']
    
    fieldsets = (
        (None, {
            'fields': ('evaluacion', 'pregunta')
        }),
        ('Respuesta', {
            'fields': ('opcion_seleccionada', 'respuesta_texto', 'puntuacion', 'fecha_respuesta')
        }),
    )


# Admin para Tipos de Evaluación
@admin.register(TipoEvaluacion)
class TipoEvaluacionAdmin(admin.ModelAdmin):
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


# Admin para Evaluaciones Personalizadas
@admin.register(EvaluacionPersonalizada)
class EvaluacionPersonalizadaAdmin(admin.ModelAdmin):
    list_display = ['nombre_proyecto', 'cliente', 'tipo_evaluacion', 'estado', 'fecha_solicitud', 'fecha_entrega_estimada']
    list_filter = ['estado', 'fecha_solicitud', 'tipo_evaluacion']
    search_fields = ['nombre_proyecto', 'descripcion', 'cliente__username']
    readonly_fields = ['fecha_solicitud']
    
    fieldsets = (
        ('Información del Proyecto', {
            'fields': ('nombre_proyecto', 'descripcion', 'tipo_evaluacion')
        }),
        ('Cliente y Estado', {
            'fields': ('cliente', 'estado')
        }),
        ('Fechas', {
            'fields': ('fecha_solicitud', 'fecha_entrega_estimada')
        }),
    )
