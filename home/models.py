from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class OurOffer(models.Model):
    title = models.CharField(verbose_name = 'Título', max_length=200, unique = True)
    description = RichTextField(verbose_name = 'Descripción')
    icon = models.CharField(verbose_name = 'Icono', max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "oferta"
        verbose_name_plural = "ofertas"
        ordering = ['title']

    def __str__(self):
        return self.title
