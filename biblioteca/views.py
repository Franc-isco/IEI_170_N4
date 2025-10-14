from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import Nacionalidad_Serializer as nacser, Autor_Serializer as autser, Comuna_Serializer as comser, Direccion_Serializer as dirser, Biblioteca_Serializer as bibser, Lector_Serializer as lecser, Categoria_Serializer as catser, Libro_Serializer as libser, Prestamo_Serializer as preser
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, Categoria, Libro, Prestamo

#def pagina_inicio(request):
    #return render(request, 'biblioteca/inicio.html')

@login_required(login_url='login')
def pagina_inicio(request):
    return render(request, 'biblioteca/inicio.html')

# Create your views here.
class Nacionalidad_ViewSet(viewsets.ModelViewSet):
    # acá creamos una QUERY a nuestra tabla, trayendo todos los campos como un objeto.
    queryset = Nacionalidad.objects.all()
    # Agregamos la clase ProgrammerSerializer que ya tiene el modelo serializado para mostrar
    serializer_class = nacser
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class NacionalidadListView(ListView): #lista de todas las nacionalidades en la basededatos
    model = Nacionalidad
    template_name = 'biblioteca/nacionalidad_list.html'

class Autor_ViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = autser
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Comuna_ViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = comser
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Direccion_ViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = dirser
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Biblioteca_ViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = bibser
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Lector_ViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = lecser
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Categoria_ViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = catser
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Libro_ViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = libser
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Prestamo_ViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = preser
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]