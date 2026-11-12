
from django.contrib import admin
from django.utils.html import format_html
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'fecha_ocurrencia',
        'lugar',
        'mostrar_imagen'
    )

    list_filter = (
        'fecha_ocurrencia',
        'lugar'
    )

    search_fields = (
        'titulo',
        'lugar',
        'descripcion'
    )

    ordering = ('-fecha_ocurrencia',)

    date_hierarchy = 'fecha_ocurrencia'

    list_per_page = 20

    fields = (
        'titulo',
        'fecha_ocurrencia',
        'lugar',
        'descripcion',
        'imagen'
    )

    @admin.display(description='Imagen')
    def mostrar_imagen(self, obj):

        if obj.imagen:
            return format_html(
                '<img src="{}" width="65" height="45" style="object-fit: cover; border-radius: 5px;" />',
                obj.imagen.url
            )

        return 'Sin imagen'


admin.site.site_header = 'Administración del Portal de Noticias SENA'
admin.site.site_title = 'Portal de Noticias'
admin.site.index_title = 'Gestión de noticias'

#@admin.register(Noticia)	Registra el modelo
#list_display	Muestra las columnas
#list_filter	Permite filtrar
#search_fields	Permite buscar
#ordering	Ordena los resultados
#date_hierarchy	Permite navegar por fechas
#list_per_page	Limita registros por página
#format_html	Presenta la imagen en HTML seguro


