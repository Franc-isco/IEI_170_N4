from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length=250, null=False)

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, null=False)
    Nacionalidad = models.CharField(max_length=50, null=False)

class Lector(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250, null=False)
    rut = models.IntegerField(null=False)
    dig_verificador = models.CharField(max_length=1, null=False)

class Autor(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField()

class Genero(models.Model):
    genero = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=250, null=False)

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250, null=False)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.IntegerField()
    copias = models.IntegerField()

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(null=False)
    fecha_devolucion = models.DateField(null=False)

