from django.db import models

class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=50, editable=False)
    subnombre = models.CharField('Nombre Corto', max_length=50, unique=True)
    activo = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Áreas de la empresa'
        ordering=['-nombre']
        unique_together=('nombre','subnombre')


    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.subnombre}"
