from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TipoConsulta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_minutos = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Tipo de Consulta"
        verbose_name_plural = "Tipos de Consulta"
    
    def __str__(self):
        return self.nombre


class Psicologo(models.Model):
    ESPECIALIDADES = [
        ('organizacional', 'Psicología Organizacional'),
        ('clinica', 'Psicología Clínica'),
        ('cognitiva', 'Psicología Cognitiva'),
        ('industrial', 'Psicología Industrial'),
        ('social', 'Psicología Social'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=20, choices=ESPECIALIDADES)
    experiencia_anos = models.IntegerField()
    descripcion = models.TextField()
    tarifa_hora = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='psicologos/', null=True, blank=True)
    
    class Meta:
        verbose_name = "Psicólogo"
        verbose_name_plural = "Psicólogos"
    
    def __str__(self):
        return f"Dr./Dra. {self.usuario.get_full_name()}"


class Consulta(models.Model):
    ESTADO_CONSULTA = [
        ('solicitada', 'Solicitada'),
        ('confirmada', 'Confirmada'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultas_cliente')
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, related_name='consultas_psicologo')
    tipo_consulta = models.ForeignKey(TipoConsulta, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_agendada = models.DateTimeField()
    duracion_minutos = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADO_CONSULTA, default='solicitada')
    motivo_consulta = models.TextField()
    notas_cliente = models.TextField(null=True, blank=True)
    notas_psicologo = models.TextField(null=True, blank=True)
    calificacion = models.IntegerField(null=True, blank=True, help_text="Calificación del 1 al 5")
    comentarios_finales = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ['-fecha_solicitud']
    
    def __str__(self):
        return f"{self.cliente.get_full_name()} - {self.psicologo.usuario.get_full_name()}"


class DisponibilidadPsicologo(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=[
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ])
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Disponibilidad del Psicólogo"
        verbose_name_plural = "Disponibilidades de Psicólogos"
        unique_together = ['psicologo', 'dia_semana', 'hora_inicio']
    
    def __str__(self):
        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        return f"{self.psicologo.usuario.get_full_name()} - {dias[self.dia_semana]} {self.hora_inicio}-{self.hora_fin}"


class MensajeConsulta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Mensaje de Consulta"
        verbose_name_plural = "Mensajes de Consulta"
        ordering = ['fecha_envio']
    
    def __str__(self):
        return f"{self.consulta} - {self.remitente.get_full_name()}"