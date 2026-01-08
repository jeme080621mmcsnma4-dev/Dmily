from django.db import models
from ckeditor.fields import RichTextField
from applications.departamento.models import Departamento

# Create your models here.

class Habilidad(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de empleados'

    def __str__(self):
        return f"{self.id} - {self.habilidad}"


class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidad)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"
