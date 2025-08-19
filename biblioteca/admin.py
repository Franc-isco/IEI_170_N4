from django.contrib import admin
from .models import Biblioteca, Nacionalidad, Lector, Autor, Genero, Libro, Prestamo 

# Register your models here.
admin.site.register(Biblioteca)
admin.site.register(Nacionalidad)
admin.site.register(Lector)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Prestamo)
