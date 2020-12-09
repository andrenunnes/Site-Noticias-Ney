from django.contrib import admin
from noticias.models import Noticia



@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "autor", "data")
    prepopulated_fields = {"slug": ("titulo",)}
