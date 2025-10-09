from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CuestionarioNOM035(models.Model):
    ESTADO_CUESTIONARIO = [
        ('borrador', 'Borrador'),
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    
    nombre = models.CharField(max_length=200)
    version = models.CharField(max_length=10)
    descripcion = models.TextField()
    estado = models.CharField(max_length=10, choices=ESTADO_CUESTIONARIO, default='borrador')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Cuestionario NOM-035"
        verbose_name_plural = "Cuestionarios NOM-035"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.nombre} v{self.version}"


class DominioNOM035(models.Model):
    cuestionario = models.ForeignKey(CuestionarioNOM035, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    orden = models.IntegerField()
    
    class Meta:
        verbose_name = "Dominio NOM-035"
        verbose_name_plural = "Dominios NOM-035"
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.cuestionario.nombre} - {self.nombre}"


class PreguntaNOM035(models.Model):
    TIPO_PREGUNTA = [
        ('likert', 'Escala Likert'),
        ('multiple', 'Opción Múltiple'),
        ('abierta', 'Respuesta Abierta'),
    ]
    
    dominio = models.ForeignKey(DominioNOM035, on_delete=models.CASCADE)
    texto = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_PREGUNTA)
    orden = models.IntegerField()
    obligatoria = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Pregunta NOM-035"
        verbose_name_plural = "Preguntas NOM-035"
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.dominio.nombre} - Pregunta {self.orden}"


class OpcionRespuesta(models.Model):
    pregunta = models.ForeignKey(PreguntaNOM035, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    valor = models.IntegerField()
    orden = models.IntegerField()
    
    class Meta:
        verbose_name = "Opción de Respuesta"
        verbose_name_plural = "Opciones de Respuesta"
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.pregunta} - {self.texto}"


class Evaluacion(models.Model):
    ESTADO_EVALUACION = [
        ('iniciada', 'Iniciada'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    cuestionario = models.ForeignKey(CuestionarioNOM035, on_delete=models.CASCADE)
    evaluado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evaluaciones_recibidas')
    evaluador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evaluaciones_realizadas')
    estado = models.CharField(max_length=15, choices=ESTADO_EVALUACION, default='iniciada')
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_completado = models.DateTimeField(null=True, blank=True)
    puntuacion_total = models.FloatField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Evaluación"
        verbose_name_plural = "Evaluaciones"
        ordering = ['-fecha_inicio']
    
    def __str__(self):
        return f"{self.evaluado.get_full_name()} - {self.cuestionario.nombre}"


class RespuestaEvaluacion(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(PreguntaNOM035, on_delete=models.CASCADE)
    opcion_seleccionada = models.ForeignKey(OpcionRespuesta, on_delete=models.CASCADE, null=True, blank=True)
    respuesta_texto = models.TextField(null=True, blank=True)
    puntuacion = models.FloatField(null=True, blank=True)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Respuesta de Evaluación"
        verbose_name_plural = "Respuestas de Evaluación"
        unique_together = ['evaluacion', 'pregunta']
    
    def __str__(self):
        return f"{self.evaluacion} - {self.pregunta}"


class TipoEvaluacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_minutos = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Tipo de Evaluación"
        verbose_name_plural = "Tipos de Evaluación"
    
    def __str__(self):
        return self.nombre


class EvaluacionPersonalizada(models.Model):
    tipo_evaluacion = models.ForeignKey(TipoEvaluacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_proyecto = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_entrega_estimada = models.DateTimeField()
    estado = models.CharField(max_length=20, default='pendiente')
    
    class Meta:
        verbose_name = "Evaluación Personalizada"
        verbose_name_plural = "Evaluaciones Personalizadas"
        ordering = ['-fecha_solicitud']
    
    def __str__(self):
        return f"{self.cliente.get_full_name()} - {self.nombre_proyecto}"