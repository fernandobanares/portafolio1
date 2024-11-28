from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen_principal = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    url_github = models.URLField(max_length=200, blank=True, null=True)
    herramientas = models.CharField(max_length=500, blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=[
        ('salud', 'Salud'),
        ('comercio', 'Comercio'),
        ('tecnologia', 'Tecnología'),
    ], default='tecnologia')

    def __str__(self):
        return self.titulo