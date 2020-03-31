from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Member(models.Model):
    name = models.CharField(verbose_name = 'Nombre', max_length = 150)
    photo = models.ImageField(verbose_name = 'Foto', upload_to = 'team/%Y/%m/%d')
    position = models.CharField(verbose_name = 'Puesto', max_length = 100)
    description = models.TextField(verbose_name = 'Descripción')
    phone = PhoneNumberField(verbose_name = 'Teléfono', unique = True)
    email = models.EmailField(verbose_name = 'Correo Electrónico', max_length = 200, unique = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "miembro del equipo"
        verbose_name_plural = "miembros del equipo"
        ordering = ['-created']

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(verbose_name = 'Nombre', max_length = 150)
    link = models.URLField(verbose_name = 'Enlace', max_length = 200)
    icon = models.CharField(verbose_name = 'Clase del Icono', max_length = 100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "red social"
        verbose_name_plural = "redes sociales"
        ordering = ['-created']

    def __str__(self):
        return self.name
