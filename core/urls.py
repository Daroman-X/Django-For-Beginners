from django.urls import path
from .views import *
app_name="core"
urlpatterns = [
    path("", Inicio.as_view(),name="inicio"),
    path("about/", Informacion.as_view(),name="acerca_de"),
]
