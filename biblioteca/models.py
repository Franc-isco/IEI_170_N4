from django.db import models
import datetime
from rut_chile import rut_chile
from django.forms import ValidationError
from datetime import date


ahora = datetime.datetime.now

# Create your models here.

def validar_rut(rut):
    valido = rut_chile.is_valid_rut(rut)
    if valido==False:
        raise ValidationError('RUT inválido.')

# 🔹 Validador de mayoría de edad (mínimo 18 años)
def validar_mayor_edad(fecha_nacimiento):
    if fecha_nacimiento is None:
        raise ValidationError('Debe ingresar una fecha de nacimiento válida.')

    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - (
        (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
    )

    if edad < 18:
        raise ValidationError('El lector debe ser mayor de 18 años.')
    
# 🔹 Validador de ISBN (formato básico ISBN-13)
def validar_isbn(isbn):
    if isbn is None or isbn == '':
        raise ValidationError('Debe ingresar un ISBN.')
    # Eliminar guiones o espacios, por si el usuario escribe algo como "978-1234567890"
    isbn_limpio = isbn.replace('-', '').replace(' ', '')
    # Debe tener solo números
    if not isbn_limpio.isdigit():
        raise ValidationError('El ISBN debe contener solo números.')
    # Debe tener exactamente 13 dígitos (ISBN-13)
    if len(isbn_limpio) != 13:
        raise ValidationError('El ISBN debe tener exactamente 13 dígitos.')


class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    nombre_comuna = models.CharField(max_length=50, null=False) 
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_comuna}"

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=255, null=False)
    nombre_nacionalidad = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_nacionalidad}"

class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False)
    calle = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=10, null=True)
    departamento = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.calle} {self.numero or ''}, {self.id_comuna.nombre_comuna}"


class Biblioteca(models.Model):
    nombre_biblioteca = models.CharField(max_length=100, null=False)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)
    web = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_biblioteca}"
    

class Lector(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, null=False)
    nombre_lector = models.CharField(max_length=255, null=False)
    rut = models.CharField(max_length=12, blank=False, unique=True, validators=[validar_rut])
    #digito_verificador = models.CharField(max_length=1, null=False)
    correo_lector = models.CharField(max_length=255, blank=True)
    fecha_nacimiento = models.DateField(blank=True, default=None, validators=[validar_mayor_edad])
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_lector} ({self.rut})"

class Autor(models.Model):
    nombre_autor = models.CharField(max_length=255, null=False)
    pseudonimo = models.CharField(max_length=50,null=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.pseudonimo:
            return f"{self.nombre_autor} ({self.pseudonimo})"
        return f"{self.nombre_autor}"

class Categoria(models.Model):
    categoria = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoria

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, null=False)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=255, null=False)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    paginas = models.IntegerField()
    copias = models.IntegerField()
    isbn = models.CharField(max_length=13, unique= True, null= False, blank= False, validators=[validar_isbn])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} — {self.id_autor.nombre_autor}"

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=False)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE, null=False)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=False)
    fecha_entrega = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Préstamo de {self.id_libro.titulo} a {self.id_lector.nombre_lector}"
    