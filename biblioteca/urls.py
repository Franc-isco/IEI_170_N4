from django.urls import path, include
from rest_framework import routers
from biblioteca import views


router = routers.DefaultRouter() 


router.register(r'nacionalidad',views.Nacionalidad_ViewSet)
router.register(r'autor',views.Autor_ViewSet)
router.register(r'comuna',views.Comuna_ViewSet)
router.register(r'direccion',views.Direccion_ViewSet)
router.register(r'biblioteca',views.Biblioteca_ViewSet)
router.register(r'lector',views.Lector_ViewSet)
router.register(r'categoria',views.Categoria_ViewSet)
router.register(r'libro',views.Libro_ViewSet)
router.register(r'prestamo',views.Prestamo_ViewSet)


urlpatterns = [
 path('', include(router.urls))
# la ruta base va a incluir todos los elementos que tengael router que hemos creado en URLS
# esta es la lista de URLS que maneja ROUTER en suselementos URLS
] 