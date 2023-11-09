from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="myindex"),
    #path("alumno<str>", views.nombre_alumno, name="alumno"),
    #path("cursos", views.cursos, name="cursos"),
]