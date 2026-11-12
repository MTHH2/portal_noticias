
from django.db import models


class Noticia(models.Model):

    titulo = models.CharField(
        max_length=200,
        verbose_name='Título'
    )

    fecha_ocurrencia = models.DateField(
        verbose_name='Fecha del acontecimiento'
    )

    lugar = models.CharField(
        max_length=150,
        verbose_name='Lugar'
    )

    descripcion = models.TextField(
        verbose_name='Descripción'
    )

    imagen = models.ImageField(
        upload_to='noticias/',
        verbose_name='Imagen'
    )

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha_ocurrencia']

    def __str__(self):
        return self.titulo

#CharField: guarda textos cortos.
#max_length: establece la cantidad máxima de caracteres.
#DateField: guarda fechas.
#TextField: permite guardar descripciones extensas.
#ImageField: permite almacenar la ruta de una imagen.
#upload_to: indica la carpeta donde se guardarán las imágenes.
#__str__: determina cómo se identifica una noticia en el panel.
#ordering: establece el orden predeterminado de los registros.

